# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 08:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20160623_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyaction',
            name='completed_timestamp',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 6, 23, 8, 54, 48, 296015)),
            preserve_default=False,
        ),
    ]
