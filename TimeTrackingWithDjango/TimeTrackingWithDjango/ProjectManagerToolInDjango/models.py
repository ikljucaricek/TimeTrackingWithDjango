from django.db import models
from django.utils.encoding import smart_unicode

#from django import forms

class Osoba(models.Model):
    id_osoba = models.AutoField(primary_key = True)
    ime_osoba = models.CharField(max_length = 50)
    prezime_osoba = models.CharField(max_length = 50)

    def __unicode__(self):
        return smart_unicode(u'%s %s' % (self.ime_osoba, self.prezime_osoba))

class Projekt(models.Model):
    id_projekt = models.AutoField(primary_key = True)
    naziv_projekt = models.CharField(max_length = 150)
    aktivan = models.BooleanField()
    datum_pocetak = models.DateField(auto_now_add = True)
    datum_zavrsetak = models.DateField(null = True, blank = True)

    def __unicode__(self):
        return smart_unicode(self.naziv_projekt)

class OsobaProjekt(models.Model):
    id = models.AutoField(primary_key = True)
    id_projekt = models.ForeignKey(Projekt)
    id_osoba = models.ForeignKey(Osoba)
    br_sati = models.IntegerField()
    datum = models.DateField(auto_now_add = True)