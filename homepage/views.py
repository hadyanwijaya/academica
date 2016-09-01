from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from kuliah.models import *
from homepage.forms import *
from akses.models import *

# Create your views here.
def login_view(request):
	if request.POST:
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		print user
		
		if user is not None:
			if user.is_active:
				try:
					akun = Akun.objects.get(user=user)
					login(request, user)
					
					print akun

					request.session['username'] = request.POST['username']
					request.session['email'] = akun.user.email

				except Exception, e:
					print e
					messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data mahasiswa, silahkan hubungi administrator')

				return redirect('/')
			else:	
				messages.add_message(request, messages.INFO, 'Anda belum terverifikasi, silahkan hubungi administrator')
		else:
			messages.add_message(request, messages.INFO, 'Akun Anda salah')

	return render(request, 'login.html')

def logout_view(request):
	logout(request)
	return redirect('/login/')

@login_required(login_url=settings.LOGIN_URL)
def daftar_nilai(request):
	akun = Akun.objects.get(user=request.user.id)
	daftar_kontrak_kuliah = KontrakKuliah.objects.filter(mahasiswa=akun.mahasiswa).order_by('-jadwal_kuliah__mulai_kuliah')
	return render(request, 'index.html', {'daftar_kontrak_kuliah':daftar_kontrak_kuliah})

@login_required(login_url=settings.LOGIN_URL)
def profil(request):
	return render(request, 'profil.html')

@login_required(login_url=settings.LOGIN_URL)
def profil_edit(request):
	user = request.user
	akun = Akun.objects.get(user=user)

	if request.method == "POST":
		print request.POST

		user_form = UserForm(request.POST)
		akun_form = AkunForm(request.POST)

		if user_form.is_valid() and akun_form.is_valid():
			user.first_name = request.POST['first_name']
			user.last_name = request.POST['last_name']
			user.email = request.POST['email']
			user.save()

			akun = Akun.objects.get(user=user)
			akun.no_telp = request.POST['no_telp']
			akun.website = request.POST['website']
			akun.alamat = request.POST['alamat']
			akun.save()
			
			return redirect('/profil')
	else:
		user_form = UserForm(instance=user)
		akun_form = AkunForm(instance=akun)

	return render(request, 'profil_edit.html', {'user_form':user_form, 'akun_form':akun_form})