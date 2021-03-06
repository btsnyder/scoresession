# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeTeam', models.CharField(max_length=100)),
                ('awayTeam', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SessionInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scores.Session')),
            ],
        ),
    ]
