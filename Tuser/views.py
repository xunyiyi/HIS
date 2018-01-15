#-*-coding=utf-8-*-
from django.shortcuts import render
import role.models
import models
import userRole.models
import roleModule.models
import module.models




# Create your views here.
def index(request):
    return render(request,"index.html")


def addUserInput(request):
    u=request.session.get("user")
    #查询所有的角色
    roles=role.models.Role.objects.all()
    c={"roles":roles}
    return render(request,"tuser/addUser.html",c)

#进入登录页面
def loginInput(request):
    return render(request, "tuser/login.html")

#登录
def login(request):
    #接收客户的用户名密码
    username=request.POST.get("username","")
    password= request.POST.get("password", "")
    u=models.Tuser.objects.filter(username=username).filter(password=password)
    print u
    if u!=None:
        request.session["user"]=username
    #创建一个list存储该用户的所有的模块权限
    mods=[]
    if len(u)>0:
        #获取用户
        tuser=u[0]
        #根据用户查询userRole对象
        urs=userRole.models.UserRole.objects.filter(uid=tuser);
        for ur in urs:
            #获取role对象
            r=ur.rid
            #根据角色对象找roleModel对象
            rms=roleModule.models.RoleModule.objects.filter(rid=r)
            for rm in rms:
                if rm.mid not in mods:
                    mods.append(module.models.Module.objects.get(id=rm.mid.id))
    c={}
    c['modules']=mods
    return render(request, "main.html", c)

#添加用户
def addUser(request):
    u=request.session.get("user")
    #判断用户是否登录
    if u==None:
        c={"msg":"请先登录"}
    return render(request,"login.html",c)

    username=request.POST.get('username',None)
    password=request.POST.get('password',None)
    rids=request.POST.getlist("rid")
    # 创建一个用户对象
    tuser = models.Tuser()
    tuser.username = username;
    tuser.password = password
    tuser.save()
    # 通过角色id查询角色对象
    for rid in rids:
        ro = role.models.Role.objects.get(id=rid)
        # 创建一个userRole对象
        ur = userRole.models.UserRole()
        ur.uid = tuser
        ur.rid = ro
        ur.save()

    c={"msg":"添加用户成功"}
    return render(request,"success.html",c)
