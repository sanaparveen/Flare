# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-01 19:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flare', '0007_auto_20160802_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='timestamp',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 8, 1, 19, 27, 19, 887000, tzinfo=utc)),
        ),
    ]