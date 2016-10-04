from django import forms
from django.contrib.auth.models import User
from akses.models import Akun

class UserForm(forms.ModelForm):
    class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']
		widgets = {
            'nama_depan': forms.TextInput(),
            'nama_belakang': forms.TextInput(),
            'email': forms.TextInput(),
        }

class AkunForm(forms.ModelForm):
	class Meta:
		model = Akun
		fields = ['no_telp', 'about_me', 'website']
		widgets = {
            'no_telp': forms.TextInput(),
            'about_me': forms.Textarea(),
            'website': forms.TextInput()
        }
