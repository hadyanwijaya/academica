from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dosen(models.Model):
	nama = models.CharField(max_length=200)
	alamat = models.TextField(blank=True)

	def __unicode__(self):
		return self.nama

class Mahasiswa(models.Model):
	nama = models.CharField(max_length=200)
	alamat = models.TextField(blank=True)

	def __unicode__(self):
		return self.nama
	
class Ruangan(models.Model):
	nama = models.CharField(max_length=100)
	deskripsi = models.TextField(blank=True)

	def __unicode__(self):
		return self.nama
	