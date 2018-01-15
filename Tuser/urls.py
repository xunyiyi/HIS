#-*-coding=utf-8-*-
"""HIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
import Tuser.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^addUserInput$",Tuser.views.addUserInput),
    url(r"^addUser$",Tuser.views.addUser),
    url(r"^loginInput$",Tuser.views.loginInput),
    url(r"^login$",Tuser.views.login),
    url(r"^$",Tuser.views.index),

]
