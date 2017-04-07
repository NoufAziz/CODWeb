# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 20:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0002_auto_20170404_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quizlet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_name', models.CharField(max_length=100, verbose_name='\u0627\u0644\u0627\u0633\u0645 \u0627\u0644\u0625\u0646\u062c\u0644\u064a\u0632\u064a')),
                ('upload_date', models.DateField(max_length=100, verbose_name='\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0625\u0636\u0627\u0641\u0629')),
                ('quizlet_url', models.URLField(max_length=100, verbose_name='\u0643\u0648\u064a\u0632\u0644\u062a')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='files.Category', verbose_name='\u0627\u0644\u062a\u0635\u0646\u064a\u0641')),
                ('contributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u0627\u0644\u0645\u0633\u0627\u0647\u0645\u0640/\u0640\u0629')),
            ],
        ),
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_name', models.CharField(max_length=100, verbose_name='\u0627\u0644\u0627\u0633\u0645 \u0627\u0644\u0625\u0646\u062c\u0644\u064a\u0632\u064a')),
                ('upload_date', models.DateField(max_length=100, verbose_name='\u062a\u0627\u0631\u064a\u062e \u0627\u0644\u0625\u0636\u0627\u0641\u0629')),
                ('youtube_url', models.URLField(max_length=100, verbose_name='\u064a\u0648\u062a\u064a\u0648\u0628')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='files.Category', verbose_name='\u0627\u0644\u062a\u0635\u0646\u064a\u0641')),
                ('contributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u0627\u0644\u0645\u0633\u0627\u0647\u0645\u0640/\u0640\u0629')),
            ],
        ),
        migrations.RemoveField(
            model_name='file',
            name='quizlet_url',
        ),
        migrations.RemoveField(
            model_name='file',
            name='youtube_url',
        ),
    ]