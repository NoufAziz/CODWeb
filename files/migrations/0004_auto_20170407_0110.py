# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 01:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_auto_20170406_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='category',
        ),
        migrations.RemoveField(
            model_name='quizlet',
            name='category',
        ),
        migrations.RemoveField(
            model_name='youtube',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]