#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Section(models.Model):
    secId=models.CharField(max_length=20)
    secName=models.CharField(max_length=30)