# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-16 20:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_message', models.TextField(default=None)),
                ('timestamp', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('creator', models.TextField()),
                ('group_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='flare.ChatGroups')),
            ],
        ),
    ]
