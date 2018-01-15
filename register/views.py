#-*-coding:utf-8 -*-
from django.shortcuts import render
import section.models
import json
from django.http import HttpResponse
# Create your views here.


def registerInput(request):
    secs=section.models.Section.objects.all()
    c={}
    c['secs']=secs
    docs=secs[0].doctor_set.all()
    print secs[0].secName
    print(docs)
    for doc in docs:
        print doc.dname
    #拿到该科室下的所有医生存到字典中传到页面
    c['docs']=docs
    return render(request,"register/register.html",c)



#通过科室找到该科室下的医生信息
def findDocsBySec(request):
    id=request.POST.get("id","");
    # #通过科室编号查询科室对象
    sec=section.models.Section.objects.get(id=id)
    print sec.secName
    # #通过科室对象查询医生对象
    docs=sec.doctor_set.all()
    #把python的医生对象转成json的医生对象
    ds=[]
    for doc in docs:
        d={}
        d.update(doc.__dict__)
        ds.append(d)
    c={}
    c['sec']=sec
    c['docs']=docs
    print ds
    return HttpResponse(ds)

