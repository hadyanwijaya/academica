from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tatausaha.models import *

# Create your models here.
class Akun(models.Model):
	mahasiswa = models.ForeignKey(Mahasiswa)
	user = models.ForeignKey(User)
	no_telp = models.CharField(max_length=50,blank=True)
	about_me = models.TextField(blank=True)
	website = models.CharField(blank=True, max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.mahasiswa.nama + " --- " + self.user.username