# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-28 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190326_1253'),
        ('tasks', '0010_task_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForTeamForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Team')),
            ],
        ),
    ]
