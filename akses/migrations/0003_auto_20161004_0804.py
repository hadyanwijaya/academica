# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-04 08:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('akses', '0002_auto_20161004_0755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='akun',
            old_name='alamat',
            new_name='about_me',
        ),
    ]
