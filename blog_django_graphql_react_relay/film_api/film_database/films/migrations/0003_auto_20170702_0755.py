# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-02 07:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_remove_film_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='year',
            new_name='air_date',
        ),
    ]
