from __future__ import unicode_literals

from django.db import models


class Palestra(models.Model):
    palestrante = models.CharField(max_length=30)
    titulo = models.CharField(max_length=20)
    data = models.DateTimeField('data da palestra')
    descricao = models.CharField(max_length=140)

class VisitaTecnica(models.Model):
    local = models.CharField(max_length=30)
    data = models.DateTimeField('data da visita')
    descricao = models.CharField(max_length=140)

class MiniCurso(models.Model):
    titulo = models.CharField(max_length=20)
    data = models.DateTimeField('data da visita')
    instrutor = models.CharField(max_length=30)
    descricao = models.CharField(max_length=140)
