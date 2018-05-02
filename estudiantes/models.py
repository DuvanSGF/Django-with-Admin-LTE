# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import GroupedForeignKey

# Create your models here.

VENADA = (
       ('0', 'Si'),
       ('1', 'No'),
)

ESTADOS = (('0', 'Activo'), ('1', 'Desactivo'))

TIPOID = (
       ('0', 'TI'),
       ('1', 'CC'),
)

class Programa(models.Model):
    id_Programa = models.AutoField(primary_key=True)
    Pr_Nombre = models.CharField(max_length=35)

    def __unicode__(self):
        return str(self.Pr_Nombre)

class Departamento(models.Model):
    Dep_Nombre = models.CharField(max_length=35)

    def __unicode__(self):
        return str(self.Dep_Nombre)

class Municipio(models.Model):
    Mun_nombre = models.CharField(max_length=35)
    Mun_departamento = models.ForeignKey(Departamento, null=True,  blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.Mun_nombre)

class Estudiante(models.Model):
    id_Estudiante = models.AutoField(primary_key=True)
    Es_Nombre = models.CharField(max_length=25)
    Es_Apellido = models.CharField(max_length=25)
    Es_TipoID = models.CharField(max_length=1, choices=TIPOID, default="0")
    Es_Identificacion = models.IntegerField()
    Es_Codigo = models.CharField(max_length=20)
    Es_Programa_ID = models.ForeignKey(Programa, null=True, blank=True, on_delete=models.CASCADE)
    Es_Departamento = models.ForeignKey(Departamento)
    Es_Municipio = GroupedForeignKey(Municipio, "Mun_departamento")
    Es_Venada = models.CharField(max_length=1, choices=VENADA, default="0")
    Es_Estado = models.CharField(max_length=1, choices=ESTADOS, default="0")
