# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0006_auto_20170422_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minicurso',
            name='inscritos',
            field=models.ManyToManyField(to='see_profile.ProfileUser'),
        ),
        migrations.AlterField(
            model_name='palestra',
            name='interesse',
            field=models.ManyToManyField(to='see_profile.ProfileUser'),
        ),
        migrations.AlterField(
            model_name='visitatecnica',
            name='inscritos',
            field=models.ManyToManyField(to='see_profile.ProfileUser'),
        ),
    ]