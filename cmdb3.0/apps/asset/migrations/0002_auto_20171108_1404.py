# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-08 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='group',
        ),
        migrations.AddField(
            model_name='asset',
            name='group',
            field=models.CharField(blank=True, max_length=30, verbose_name='\u6240\u5c5e\u4e3b\u673a\u7ec4'),
        ),
    ]
