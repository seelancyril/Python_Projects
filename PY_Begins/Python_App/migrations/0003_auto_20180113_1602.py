# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-13 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Python_App', '0002_auto_20180113_1539'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
