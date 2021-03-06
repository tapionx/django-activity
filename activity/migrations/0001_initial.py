# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=512, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityRegistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=512)),
                ('reference', models.CharField(max_length=512, null=True)),
                ('start_time', models.PositiveIntegerField(default=None, null=True)),
                ('end', models.PositiveIntegerField(default=100)),
                ('done', models.PositiveIntegerField(default=0)),
                ('timeout', models.PositiveIntegerField(null=True)),
                ('msg', models.TextField(default='nessun aggiornamento in corso')),
                ('last_update_time', models.PositiveIntegerField(null=True)),
                ('is_locked', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('consumed', models.BooleanField(default=False)),
                ('return_code', models.CharField(blank=True, default=b'', max_length=512)),
                ('note', models.TextField(blank=True, default=b'')),
            ],
            options={
                'get_latest_by': 'last_update_time',
            },
        ),
        migrations.AddField(
            model_name='activejob',
            name='activity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='activity.ActivityRegistry'),
        ),
    ]
