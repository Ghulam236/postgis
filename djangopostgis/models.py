from __future__ import unicode_literals
from django.db.models import Manager 
from django.db import models

from django.contrib.gis.db import models




# Create your models here.
class Incidences(models.Model):
    name =models.CharField(max_length=70)
    location=models.PointField(srid=4326)
    objects =models.Manager()

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural="Incidences"
class country(models.Model):
    name_1 = models.CharField(max_length=75)
    name_0 = models.CharField(max_length=75)
    id_0 = models.BigIntegerField()
    iso = models.CharField(max_length=3)
    # name_0 = models.CharField(max_length=75)
    id_1 = models.BigIntegerField()
    # name_1 = models.CharField(max_length=75)
    type_1 = models.CharField(max_length=50)
    engtype_1 = models.CharField(max_length=50)
    # nl_name_1 = models.CharField(max_length=50)
    # varname_1 = models.CharField(max_length=150)
    geom = models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.country

class Indstates(models.Model):
    id_0 = models.BigIntegerField()
    iso = models.CharField(max_length=3)
    name_0 = models.CharField(max_length=75)
    id_1 = models.BigIntegerField()
    name_1 = models.CharField(max_length=75)
    id_2 = models.BigIntegerField()
    name_2 = models.CharField(max_length=75)
    type_2 = models.CharField(max_length=50)
    engtype_2 = models.CharField(max_length=50)
    # nl_name_2 = models.CharField(max_length=75)
    # varname_2 = models.CharField(max_length=150)
    geom = models.MultiPolygonField(srid=4326)
    def __unicode__(self):
        return self.Indstates
