from __future__ import unicode_literals
from django.db import models
import os
from django.conf import settings
from see_profile import models as profiles

class Palestra(models.Model):
    palestrante = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    data = models.DateTimeField('data da palestra')
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(upload_to='palestras', default='no_photo.png')
    interesse = models.ManyToManyField(profiles.ProfileUser)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('data',)

class VisitaTecnica(models.Model):
    local = models.CharField(max_length=50)
    data = models.DateTimeField('data da visita')
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(upload_to='visitas', default='media/no_photo.png')
    inscritos = models.ManyToManyField(profiles.ProfileUser)

    def __str__(self):
        return self.local

    class Meta:
        ordering = ('data',)

class MiniCurso(models.Model):
    titulo = models.CharField(max_length=50)
    data = models.DateTimeField('data do minicurso')
    instrutor = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    imagem = models.ImageField(upload_to='minicursos', default='no_photo.png')
    inscritos = models.ManyToManyField(profiles.ProfileUser)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('data',)
