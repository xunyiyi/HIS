from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Module(models.Model):
    mName=models.CharField(max_length=20)
    mUrl=models.CharField(max_length=200)