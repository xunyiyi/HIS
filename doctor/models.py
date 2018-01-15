#-*-coding:utf-8-*-
from __future__ import unicode_literals

from django.db import models
import section.models

# Create your models here.
#所有的模型都要继承models.Model
class Doctor(models.Model):
    #医生姓名
    dname=models.CharField(max_length=20)
    #证件类型
    papersType=models.IntegerField()
    #证件号
    papersNum=models.CharField(max_length=18)
    #手机
    phone=models.CharField(max_length=11)
    #座机
    telephone=models.CharField(max_length=11)
    #性别
    sex=models.IntegerField()
    #年龄
    age=models.IntegerField()
    #出生年月
    birthday=models.DateField(null=True)
    #电子邮箱
    email=models.EmailField()
    #科室的主键
    sectionId=models.ForeignKey(section.models.Section,null=True,on_delete=models.SET_NULL)
    #学历
    degree=models.IntegerField()
    #备注
    remark=models.CharField(max_length=50)
    #入职时间
    hireDate=models.DateField()

