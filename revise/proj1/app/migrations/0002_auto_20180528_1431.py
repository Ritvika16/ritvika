# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 14:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='type',
            new_name='user_type',
        ),
    ]
