# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-09 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0005_auto_20171109_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='brand',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='\u786c\u4ef6\u5382\u5546\u578b\u53f7'),
        ),
        migrations.AddField(
            model_name='asset',
            name='sn',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='SN\u7f16\u53f7'),
        ),
    ]
