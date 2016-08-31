from __future__ import unicode_literals

from django.db import models
from tatausaha.models import *

# Create your models here.
class MataKuliah(models.Model):
	nama = models.CharField(max_length=200)
	deskripsi = models.TextField(blank=True)

	def __unicode__(self):
		return self.nama
	

class JadwalKuliah(models.Model):
	# choice field untuk semester: Semester 1, Semester 2, Semester 3, etc.
	nama = models.CharField(max_length=200)
	deskripsi = models.TextField(blank=True)
	dosen = models.ForeignKey(Dosen)
	kelas = models.ForeignKey(Ruangan)
	mulai_kuliah = models.TimeField(blank=True)
	akhir_kuliah = models.TimeField(blank=True)
	mulai_kontrak = models.DateField(blank=True)
	akhir_kontrak = models.DateField(blank=True)
	tahun = models.IntegerField(blank=True)
	
	def __unicode__(self):
		return self.nama
	
class KontrakKuliah(models.Model):
	SEMESTER_TYPE = (
        ("semester_1","Semester 1"),
        ("semester_2","Semester 2"),
        ("semester_3","Semester 3"),
        ("semester_4","Semester 4"),
        ("semester_5","Semester 5"),
        ("semester_6","Semester 6"),
        ("semester_7","Semester 7"),
        ("semester_8","Semester 8"),
        ("semester_9","Semester 9"),
        ("semester_10","Semester 10"),
        ("semester_11","Semester 11"),
        ("semester_12","Semester 12"),
        ("semester_pendek","Semester Pendek"),
    )

	jadwal_kuliah = models.ForeignKey(JadwalKuliah)
	mahasiswa = models.ForeignKey(Mahasiswa)
	nilai_akhir = models.CharField(max_length=2)
	semester = models.CharField(max_length=50, choices=SEMESTER_TYPE, default="semester_1")
	
	def __unicode__(self):
		return "%s mengontrak %s" %(self.mahasiswa.nama, self.jadwal_kuliah.nama)
	