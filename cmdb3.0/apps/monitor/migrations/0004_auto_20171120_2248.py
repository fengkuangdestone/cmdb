# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-20 22:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20171120_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitorinfo',
            name='ip',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to='asset.Asset', verbose_name='\u5173\u8054\u4e3b\u673a'),
        ),
    ]
