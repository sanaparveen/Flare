# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-03 13:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flare', '0011_auto_20160803_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='timestamp',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2016, 8, 3, 13, 26, 24, 839000, tzinfo=utc)),
        ),
    ]
