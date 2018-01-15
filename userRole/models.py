from __future__ import unicode_literals

from django.db import models
from role.models import Role
from Tuser.models import Tuser

# Create your models here.
class UserRole(models.Model):
    uid=models.ForeignKey(Tuser,null=True)
    rid=models.ForeignKey(Role,null=True)