# -*- coding: utf-8  -*-
from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    name = models.CharField("االاسم", max_length=100)
    code = models.CharField("اختصار السنة الدراسية", max_length=2, null=True, blank=True)
    photo = models.URLField("الصورة", null=True, blank=True)
    slug = models.SlugField("الرابط", max_length=40)
    def __unicode__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField("الاسم", max_length=100)
    code = models.CharField("رمز المادة", max_length=7, null=True, blank=True)
    photo = models.URLField("الصورة", null=True, blank=True)
    description = models.TextField("الوصف", max_length=1000)
    date = models.DateField("التاريخ", auto_now=False)

    def __unicode__(self):
        return self.name