#-*-coding:utf-8-*-
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Count
import  json
import section.models


import models
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
#导入分页程序模块
from django.core.paginator import Paginator

# Create your views here.
#响应addDoc页面
def addDocInput(request):
    #查询所有的科室并赋值给addDoc.html模板
    sections=section.models.Section.objects.all()
    c={}
    c['sections']=sections
    return render(request, "doctor/addDoc.html", c)

#医生的添加
def addDoc(request):
    #接收客户端传递的参数值
    #姓名
    dname=request.POST['dname']
    #证件类型
    papersType=request.POST['papersType']
    #证件号
    papersNum=request.POST['papersNum']
    #手机号
    phone=request.POST['phone']
    #座机号
    telephone=request.POST['telephone']
    #性别
    sex=request.POST['sex']
    #年龄
    age=request.POST['age']
    #生日
    birthday=request.POST['birthday']
    #邮箱
    email=request.POST['email']
    #科室编号
    # try:
    #     sectionId=request.POST['sectionId']
    # except:
    #     sectionId=None
    sectionId=request.POST.get('sectionId',None)
    #学历
    degree=request.POST['degree']
    #备注
    remark=request.POST['remark']
    #入职时间
    hireDate=request.POST['hireDate']
    #创建一个doctor对象
    doc=models.Doctor()
    doc.dname=dname
    doc.papersType=papersType
    doc.papersNum=papersNum
    doc.phone=phone
    doc.telephone=telephone
    doc.sex=sex
    doc.age=age
    doc.birthday=birthday
    doc.email=email
    #给该医生对象设置一个科室对象
    if sectionId!=None:
        doc.sectionId=section.models.Section.objects.get(id=sectionId)
    doc.degree=degree
    doc.hireDate=hireDate
    #保存doc对象
    doc.save()
    c={}
    c['msg']="添加成功"
    #给客户端响应
    return render(request, "doctor/../templates/success.html", c)


#查询所有医生
def listDoc(request):
    doctors=models.Doctor.objects.all();
    c={}
    c['docs']=doctors;
    return render(request, "doctor/listDoc.html", c)


#分页查询
def listDocByPager(request):
    u=request.session.get('user')
    if u == None:
        c = {"msg": "请先登录"}
        return render(request, "tuser/login.html", c)
    try:
        sex = request.GET.get('sex',"男")
        print sex
    except MultiValueDictKeyError:
        sex=""
        print sex

    if sex==None or sex=="":
        # 查询到所有的医生
        doctors = models.Doctor.objects.all();
    else:
        s = 0
        if sex == '男':
            s = 0
        elif sex == '女':
            s = 1
        doctors=models.Doctor.objects.filter(sex=s)

    #获取客户端传递的当前页码
    try:
        currentPage=request.GET['currentPage']
    except:
        currentPage=1

    #创建一个分页对象
    pager=Paginator(doctors,5)
    #获取某一页的数据（currentPage页）
    docs=pager.page(currentPage)
    c={}
    #把当前页的医生列表存储到字典中并传递给listDoc.html模板中
    c['docs']=docs
    #页面范围
    #获取当前页
    cp=currentPage
    c['cp']=int(cp)
    c['sex']=sex
    c['pager']=pager
    return render(request, "doctor/listDoc.html", c)




#删除医生
def delDoc(request):
    #接收客户端传递的主键id
    did=request.GET['id']
    #通过主键查询到要删除的对象
    doc=models.Doctor.objects.get(id=did)
    #删除对象
    doc.delete()
    return listDoc(request)


#根据主键查询一个医生
def findDocById(request):
    #接收客户端传递的主键id
    did=request.GET['id']
    #通过id查询一个医生对象
    doc=models.Doctor.objects.get(id=did)
    c={}
    c['doc']=doc
    secs=section.models.Section.objects.all()
    c['secs']=secs
    #响应updateDoc.html并传递要修改的医生的信息
    return render(request, "doctor/updateDoc.html", c)





#修改医生
def updateDoc(request):
    #接收客户端传递的参数值
    #编号
    id=request.POST['id']
    #姓名
    dname=request.POST['dname']
    #证件类型
    papersType=request.POST['papersType']
    #证件号
    papersNum=request.POST['papersNum']
    #手机号
    phone=request.POST['phone']
    #座机号
    telephone=request.POST['telephone']
    #性别
    sex=request.POST['sex']
    #年龄
    age=request.POST['age']
    #生日
    birthday=request.POST['birthday']
    #邮箱
    email=request.POST['email']
    #科室编号
    sectionId=request.POST['sectionId']
    #学历
    degree=request.POST['degree']
    #备注
    remark=request.POST['remark']
    #入职时间
    hireDate=request.POST['hireDate']

    #根据id获取到原来的对象
    doc=models.Doctor.objects.get(id=id)
    doc.dname=dname
    doc.papersType=papersType
    doc.papersNum=papersNum
    doc.phone=phone
    doc.telephone=telephone
    doc.sex=sex
    doc.age=age
    doc.birthday=birthday
    doc.email=email
    doc.sectionId=section.models.Section.objects.get(id=int(sectionId))
    doc.degree=degree
    doc.hireDate=hireDate
    #修改doc对象
    doc.save()
    #给客户端响应
    return listDoc(request)


def showDegree(request):
    #获取所有的各个学历的人的比例
    return render(request, "doctor/degree.html")

#查询男女比例
def showSex(request):
    nanCount=models.Doctor.objects.filter(sex=0).aggregate(c=Count("sex"))
    nvCount=models.Doctor.objects.filter(sex=1).aggregate(c=Count("sex"))
    nan= int(nanCount['c']*1.0/(nanCount['c']+nvCount['c'])*100)
    nv= int(nvCount['c']*1.0/(nanCount['c']+nvCount['c'])*100)
    c={}
    ni='''[{
      type: 'pie',
      name: 'Browser share',
      data: [['男',%d],['女',%d]]
   }];  
    '''%(nan,nv)
    series=json.dumps(ni)
    print series
    c['series']=series
    return render(request, "doctor/showSex.html", c)




#通过医生的姓名查询医生对象
def findDocByDname(request):
    dname=request.GET.get("dname","")
    docs=models.Doctor.objects.filter(dname=dname)
    if len(docs)>0:
        #响应医生已经存在
        return HttpResponse("响应医生已经存在")
    else:
        # 响应医生不存在，可用
        return HttpResponse("医生不存在，可用")
