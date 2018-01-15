#-*-coding=utf-8-*-
from django.shortcuts import render
import models
# Create your views here.
from django.core.paginator import Paginator

def addSectionInput(request):
    return render(request,"section/addSection.html")


#添加
def addSection(request):
    secId=request.POST['secId']
    secName=request.POST['secName']
    #创建科室对象
    section=models.Section()
    section.secId=secId;
    section.secName=secName

    c={}
    #保存科室对象
    try:
       section.save()
       c['msg']="添加科室成功"
       return render(request, "doctor/../templates/success.html", c)
    except:
        c['eirrorMsg']="添加科室失败"
        return render(request,"section/addSection.html",c)


#查询所有科室信息
def listSectionByPager(request):
    #从客户端接收要查询的页面数
    try:
        currentPage=request.GET['currentPage']
    except:
        currentPage=1
    #接收客户的查询条件科室的名字
    try:
        secName=request.GET['secName']
    except:
        secName=""
    if secName==None or secName=='':
        secs=models.Section.objects.all()
    else:
        secs=models.Section.objects.filter(secName=secName)

    pager=Paginator(secs,5)
    #传入当前页,返回当前页的数据
    sections=pager.page(currentPage)
    c={}
    c['sections']=sections
    c['cp']=int(currentPage)
    c['pager']=pager
    c['secName']=secName
    #响应模板数据并传入参数
    return render(request,"section/listSection.html",c)


def delSection(request):
    id=request.GET['id']
    #通过id查询要删除的科室，并删除
    sec=models.Section.objects.get(id=id)
    sec.delete()
    return listSectionByPager(request);

