# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-28 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180528_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('author_name', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=500)),
                ('copies', models.CharField(max_length=50)),
            ],
        ),
    ]
