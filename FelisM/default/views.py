# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import json
from default.models import Device, History

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import smtplib
from email.mime.text import MIMEText
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

# Create your views here.


def gethomepage(request):
    return render(request, 'Cover.html')


# history返回dashboard时的页面重定向
def returndashboard(request):
    return render(request, 'Dashboard.html')


@login_required()
def getdashboard(request):
    user = request.user.username
    deviceset = Device.objects.filter(user=user)
    devicelist = []
    for item in deviceset:
        if item.physicalquantity > item.alertline and item.sw is True:
            item.alert = True
        else:
            item.alert = False
        if item.sw is True:
            item.onoff = "on"
        else:
            item.onoff = "off"
        temp = {"id": item.id, "user": user, "identifier": item.identifier, "name": item.name,
                "physicalquantity": item.physicalquantity, "updatetime": item.updatetime,
                "alertline": item.alertline, "alert": item.alert, "sw": item.sw, "onoff": item.onoff}
        # print(item.switch)
        devicelist.append(temp)
    res = {"devicelist": devicelist}
    return JsonResponse(res)


@login_required()
def gethistory(request):
    user = request.user.username
    historylist = History.objects.filter(user=user)
    return render(request, 'History.html', {'historylist': historylist})


@login_required()
def search(request):
    user = request.user.username
    search = json.loads(request.body)
    searchsn = search['sn']
    searchitem = Device.objects.get(user=user, identifier=searchsn)
    resdevice = {"id": searchitem.id, "user": user, "identifier": searchsn, "name": searchitem.name,
                 "physicalquantity": searchitem.physicalquantity, "updatetime": searchitem.updatetime,
                 "Alert": searchitem.alert, "sw": searchitem.sw,
                 "onoff": searchitem.onoff}
    res = {"success": "true", "device": resdevice}
    return JsonResponse(res)


@login_required()
def adddevice(request):
    user = request.user.username
    device = json.loads(request.body)
    deviceuser = user
    deviceidentifier = device['sn']
    devicename = device['name']
    devicephysicalquantity = 0  # 改！！！！！device['physicalquantity']
    devicealertline = device['alertline']
    devicealert = False  # device['alert']
    deviceswitch = False   # !!!!!!!!!!
    deviceonoff = "off"
    newdevice = Device.objects.create(user=deviceuser, identifier=deviceidentifier, name=devicename,
                                      physicalquantity=devicephysicalquantity, alertline=devicealertline, alert=devicealert, sw=deviceswitch, onoff=deviceonoff)
    resdevice = {"id": newdevice.id, "user": deviceuser, "identifier": deviceidentifier,
                 "name": devicename, "physicalquantity": devicephysicalquantity, "alertline": devicealertline,
                 "alert": devicealert, "sw": deviceswitch, "onoff": deviceonoff}
    res = {"success": "true", "device": resdevice}
    return JsonResponse(res)


@login_required()
def editdevice(request):
    user = request.user.username
    device = json.loads(request.body)
    id = device['id']
    user = user
    identifier = device['sn']
    name = device['name']                  # 只可更改名字和编号和报警阈值
    alertline = device['alertline']
    adevice = Device.objects.get(id=id)
    adevice.identifier = identifier
    adevice.name = name
    adevice.alertline = alertline
    adevice.save()
    resdevice = {'id': id, "user": user, "identifier": identifier, "name": name, "alertline": alertline}
    res = {"success": "true", "device": resdevice}
    return JsonResponse(res)


@login_required()
def switch(request):
    user = request.user.username
    device = json.loads(request.body)
    id = device['id']
    switch = device['sw']
    adevice = Device.objects.get(id=id)
    if switch == True:
        adevice.sw = True
        adevice.onoff = "on"
    else:
        adevice.sw = False
        adevice.onoff = "off"
    adevice.save()
    resdevice = {'id': id, "user": user, "switch": switch, "onoff": adevice.onoff}
    print(switch)
    res = {"success": "true", "device": resdevice}
    return JsonResponse(res)


@login_required()
def deldevice(request):
    id = request.GET['id']
    Device.objects.get(id=id).delete()
    res = {"success": "true"}
    return JsonResponse(res)


@login_required()
def sendemail(request):
    some_user = request.user
    email_adderss = some_user.email
    send_mail('subject', 'this is the message of email', 'lyra_malfoy@sina.com',
                  [email_adderss], fail_silently=False)
    res = {"success": "true"}
    return JsonResponse(res)


def mylogin(request):
    if request.method == 'GET':
        return render(request, 'Login.html')
    elif request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['userPassword']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                owner = user.username
                devicelist = Device.objects.filter(user=owner)
                print(owner)
                print("Succeed")
                return render(request, 'Dashboard.html', {'devicelist': devicelist})
                # 登录成功，跳转到设备列表页面
            else:
                print("Useris not active")
                return render(request, 'Cover.html')
                # 待修改，仍留在登录页面，如何使用Angularjs显示错误信息
        else:
            print("User is None")
            return render(request, 'Cover.html')
            # 待修改，仍留在登录页面，如何使用Angularjs显示错误信息


def mylogout(request):
    logout(request)
    return HttpResponseRedirect("/")    # 应重定向到cover


def myregister(request):
    if request.method == 'GET':
        return render(request, 'Regist.html')
    elif request.method == 'POST':
        username = request.POST['userName']
        useremail = request.POST['userEmail']
        password = request.POST['userPassword']
        print(username)
        print(useremail)
        print(password)
        namecheck = User.objects.filter(email=username)
        if len(namecheck) > 0:
            print("User is existed")
            return render(request, 'Regist.html')
            # 用户名已存在，如何用Angularjs
        else:
            nuser = User()
            nuser.username = username
            nuser.email = useremail
            nuser.set_password(password)
            nuser.save()
            return render(request, 'Login.html')
            # 注册成功，返回登录界面?
