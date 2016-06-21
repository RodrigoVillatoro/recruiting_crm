# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20160621_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(db_index=True, max_length=31, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='job',
            unique_together=set([]),
        ),
    ]
