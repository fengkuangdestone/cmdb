# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-21 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0005_auto_20171121_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitorinfo',
            name='ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.Asset', to_field='ip', verbose_name='\u5173\u8054\u4e3b\u673a'),
        ),
    ]