# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-22 10:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duser', '0011_remove_dctusermanger_group'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserGroup',
            new_name='AuthGroupManage',
        ),
        migrations.AlterModelTable(
            name='authgroupmanage',
            table='dct_group',
        ),
    ]
