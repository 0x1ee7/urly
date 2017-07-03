# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-03 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('url', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('target', models.URLField(blank=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
