# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-23 15:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duser', '0019_auto_20171122_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dctusermanger',
            name='group',
        ),
    ]
