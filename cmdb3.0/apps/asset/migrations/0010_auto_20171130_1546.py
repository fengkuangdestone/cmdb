# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-30 15:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0009_auto_20171121_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100, verbose_name='\u4e0a\u4f20\u56fe\u7247\u5730\u5740')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'db_table': 'upload',
                'verbose_name': '\u6587\u4ef6\u4e0a\u4f20url',
                'verbose_name_plural': '\u6587\u4ef6\u4e0a\u4f20url',
            },
        ),
        migrations.AlterModelTable(
            name='asset',
            table='assets',
        ),
    ]