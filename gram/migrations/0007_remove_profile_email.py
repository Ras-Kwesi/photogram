# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-07 13:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0006_auto_20181006_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
