# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-03 16:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='life_expectancy',
            new_name='life_expecttancy',
        ),
    ]
