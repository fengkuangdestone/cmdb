# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-11-21 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duser', '0005_auto_20171121_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dctusermanger',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', to_field='name', verbose_name='\u6388\u6743\u7ec4'),
        ),
        migrations.DeleteModel(
            name='UserGroup',
        ),
    ]
