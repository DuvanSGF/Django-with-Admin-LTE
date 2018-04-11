# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
# Create your models here.

VENADA = (
       ('0', 'Si'),
       ('1', 'No'),
)

ESTADOS = (('0', 'Activo'), ('1', 'Desactivo'))

class Programa(models.Model):
    id_Programa = models.AutoField(primary_key=True)
    Pr_Nombre = models.CharField(max_length=35)

    def __str__(self):
        return '{}'.format(self.Pr_Nombre)

class Departamento(models.Model):
    id_Departamento = models.AutoField(primary_key=True)
    Dep_Nombre = models.CharField(max_length=35)

    def __str__(self):
        return '{}'.format(self.Dep_Nombre)

class Municipio(models.Model):
    id_Municipio = models.AutoField(primary_key=True)
    Mun_nombre = models.CharField(max_length=35)
    Mun_departamento_id = models.ForeignKey(Departamento)

    def __str__(self):
        return '{0}'.format(self.Mun_nombre)

class Estudiante(models.Model):
    id_Estudiante = models.AutoField(primary_key=True)
    Es_Nombre = models.CharField(max_length=25)
    Es_Apellido = models.CharField(max_length=25)
    Es_Codigo = models.CharField(max_length=20)
    Es_Programa_ID = models.ForeignKey(Programa, null=True, blank=True, on_delete=models.CASCADE)
    Es_Departamento_ID = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.CASCADE)
    Es_Municipio_ID = models.ForeignKey(Municipio, null=True, blank=True, on_delete=models.CASCADE)
    Es_Venada = models.CharField(max_length=1, choices=VENADA, default="0")
    Es_Estado = models.CharField(max_length=1, choices=ESTADOS, default="0")
