# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-09 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pethub', '0010_auto_20180309_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default='', max_length=100),
        ),
    ]
