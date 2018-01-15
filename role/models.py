from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Role(models.Model):
    rid=models.CharField(max_length=20)
    rname=models.CharField(max_length=20)