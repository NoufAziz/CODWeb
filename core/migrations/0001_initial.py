# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u0627\u0644\u0627\u0633\u0645')),
                ('code', models.CharField(max_length=7, verbose_name='\u0627\u0644\u0627\u0633\u0645')),
                ('description', models.TextField(max_length=1000, verbose_name='\u0627\u0644\u0648\u0635\u0641')),
                ('date', models.DateField(verbose_name='\u0627\u0644\u062a\u0627\u0631\u064a\u062e')),
            ],
        ),
    ]