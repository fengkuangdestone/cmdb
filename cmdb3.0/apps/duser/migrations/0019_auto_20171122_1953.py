# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-22 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duser', '0018_auto_20171122_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dctusermanger',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='duser.AuthGroupManage', to_field='name', verbose_name='\u6388\u6743\u7ec4'),
        ),
    ]