# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-08 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_auto_20171108_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='ip',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='\u4e3b\u673aIP'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='port',
            field=models.IntegerField(blank=True, default=22, null=True, verbose_name='\u7aef\u53e3\u53f7'),
        ),
    ]
