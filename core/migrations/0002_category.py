# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u0627\u0627\u0644\u0627\u0633\u0645')),
                ('photo', models.ImageField(upload_to=b'', verbose_name='\u0627\u0644\u0635\u0648\u0631\u0629')),
                ('slug', models.SlugField(max_length=40, verbose_name='\u0627\u0644\u0631\u0627\u0628\u0637')),
            ],
        ),
    ]