# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-21 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_auto_20171121_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitorinfo',
            name='ip',
            field=models.CharField(max_length=30, verbose_name='\u5173\u8054\u4e3b\u673a'),
        ),
    ]
