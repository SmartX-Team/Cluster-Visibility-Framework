# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-04 04:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('url', models.URLField()),
                ('created_at', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
