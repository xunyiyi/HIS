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
from django.conf.urls import url
from django.contrib import admin
import doctor.views

urlpatterns = [
    url(r'^addDocInput$',doctor.views.addDocInput),
    url(r'^addDoc$',doctor.views.addDoc),
    url(r'^listDoc$',doctor.views.listDoc),
    url(r'^listDocByPager$',doctor.views.listDocByPager),
    url(r'^delDoc$',doctor.views.delDoc),
    url(r'^findDocById$',doctor.views.findDocById),
    url(r'^updateDoc$',doctor.views.updateDoc),
    url(r'^showSex$',doctor.views.showSex),
    url(r'^showDegree$',doctor.views.showDegree),
    url(r'^findDocByDname$',doctor.views.findDocByDname),

]
