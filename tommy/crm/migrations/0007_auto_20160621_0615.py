# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20160618_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
    ]