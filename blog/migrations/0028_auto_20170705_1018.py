# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 07:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20170705_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.UserProfile'),
        ),
    ]
