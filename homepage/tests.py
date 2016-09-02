from django.test import TestCase, Client
from django.contrib.auth.models import User

from akses.models import *
from tatausaha.models import *


"""
coverage run --rcfile='.coveragerc' --source='.' manage.py test

DJANGO_SETTINGS_MODULE=academica.settings coverage html --rcfile='.coveragerc'

"""

# Create your tests here.
class HomepageTest(TestCase):
	def setUp(self):
		user = User.objects.create_user('ridwanbejo', 'rahasia123')
		user.email = "ridwanbejo@gmail.com"
		user.save()

		mahasiswa = Mahasiswa.objects.create(nama="Ridwan Bejo")
		mahasiswa.save()

		akun = Akun.objects.create(mahasiswa=mahasiswa, user=user, no_telp="7501234", alamat="bandung", website="http://poss.cs.upi.edu")
		akun.save()

		self.user = user
		self.client = Client()

	def test_view_login(self):
		response = self.client.get('/login/')
		self.assertEqual(response.status_code, 200)

	def test_do_login(self):
		response = self.client.post('/login/', {'username':'ridwanbejo', 'password':'rahasia123'}, follow=True)
		self.assertEqual(response.status_code, 200)
	
	def test_view_daftar_nilai(self):
		self.client.login(username='ridwanbejo', password='rahasia123')
		response = self.client.get('/', follow=True)
		self.assertEqual(response.status_code, 200)	

	def test_view_profil(self):
		self.client.login(username='ridwanbejo', password='rahasia123')
		response = self.client.get('/profil/', follow=True)
		self.assertEqual(response.status_code, 200)	
	
	def test_view_edit_profil(self):
		self.client.login(username='ridwanbejo', password='rahasia123')
		response = self.client.get('/profil/edit', follow=True)
		self.assertEqual(response.status_code, 200)	
	
	def test_do_edit_profil(self):
		self.client.login(username='ridwanbejo', password='rahasia123')
		response = self.client.post('/profil/edit', {
					'first_name':'ridwan',
					'last_name':'fajar',
					'email':'ridwanfajar@gmail.com',
					'alamat':'bojong soang',
					'no_telp':'7501234',
					'website':'http://www.example.com'
			} ,follow=True)
		
		self.assertEqual(response.status_code, 200)	
		
	def test_do_logout(self):
		self.client.login(username='ridwanbejo', password='rahasia123')
		response = self.client.get('/logout/')
		self.assertEqual(response.status_code, 302)