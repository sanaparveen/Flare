# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-03 13:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flare', '0009_auto_20160802_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='timestamp',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 8, 3, 13, 7, 15, 24000, tzinfo=utc)),
        ),
    ]
