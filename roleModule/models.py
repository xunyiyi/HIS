from __future__ import unicode_literals

from django.db import models
from role.models import Role
from module.models import Module
# Create your models here.
class RoleModule(models.Model):
    rid=models.ForeignKey(Role,null=True)
    mid=models.ForeignKey(Module,null=True)