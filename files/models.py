# -*- coding: utf-8  -*-
from __future__ import unicode_literals
#from django.contrib.auth.models import User
from django.db import models
from core.models import Category


class Document(models.Model):
    en_name = models.CharField("الاسم الإنجليزي", max_length=100)
    document = models.FileField("الملف", upload_to='documents/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField("تاريخ الإضافة", auto_now_add=True)
    #contributor = models.ForeignKey(User, verbose_name="المساهمـ/ـة", null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="التصنيف", blank=True, null=True)
    def __unicode__(self):
        return self.en_name

class Youtube(models.Model):
    en_name = models.CharField("الاسم الإنجليزي", max_length=100)
    upload_date = models.DateField("تاريخ الإضافة", max_length=100)
    youtube_url = models.URLField("يوتيوب", max_length=100)
    #contributor = models.ForeignKey(User, verbose_name="المساهمـ/ـة", null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="التصنيف", blank=True, null=True)
    def __unicode__(self):
        return self.en_name

class Quizlet(models.Model):
    en_name = models.CharField("الاسم الإنجليزي", max_length=100)
    upload_date = models.DateField("تاريخ الإضافة", max_length=100)
    quizlet_url = models.URLField("كويزلت", max_length=100)
    #contributor = models.ForeignKey(User, verbose_name="المساهمـ/ـة", null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="التصنيف", blank=True, null=True)
    def __unicode__(self):
        return self.en_name

class Pending(models.Model):
    upload_date = models.DateTimeField("تاريخ الرفع", auto_now=True)
    #contributor = models.ForeignKey(User, verbose_name="المساهمـ/ـة")
    file = models.ForeignKey(Document, verbose_name="الملف")
    status_choices = [('SUB', 'أرسل'), ('PUB', 'منشور'), ('REJ', 'مرفوض')]
    status = models.CharField("الحالة", max_length=3, choices=status_choices, default='AVL')
    #def __unicode__(self):
        #return "{}'s pending of {}".format(contributor.username, file.en_name)
