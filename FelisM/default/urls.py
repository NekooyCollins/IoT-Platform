# coding=utf-8

from django.conf.urls import url
from .import views
urlpatterns = [
    url(r'^$', views.gethomepage),         # 进入主页
    # url(r'^getlogin/$', views.getlogin),   # 进入登录页面
    url(r'^login/$', views.mylogin),       # 登录
    url(r'^list/$', views.getdashboard),   # 获取设备列表
    url(r'^history/$', views.gethistory),  # 获取历史记录
    url(r'^dashboard/$', views.returndashboard),  # 从历史记录返回dashboard
    url(r'^search/$', views.search),       # 按编号搜索设备
    url(r'^update/$', views.getdashboard),  # 实时更新设备状态
    url(r'^add/$', views.adddevice),       # 添加设备
    url(r'^del/$', views.deldevice),       # 删除设备
    url(r'^edit/$', views.editdevice),     # 编辑设备
    url(r'^switch/$', views.switch),       # 设备开关控制
    url(r'^logout/$', views.mylogout),     # 注销登录
    url(r'^register/$', views.myregister),  # 注册用户
    url(r'^sendemail/$', views.sendemail)   # 发送报警邮件
]
