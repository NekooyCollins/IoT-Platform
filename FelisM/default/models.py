# coding=utf-8

from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Device(models.Model):
    user = models.CharField(max_length=50)        # 设备所属用户
    identifier = models.CharField(max_length=20)  # 设备编号
    name = models.CharField(max_length=20)        # 设备名称
    physicalquantity = models.DecimalField(max_digits=4, decimal_places=2)      # 设备测得的物理量，如何设置
    updatetime = models.DateTimeField(auto_now=True)           # 设备最近更新时间
    alertline = models.DecimalField(max_digits=4, decimal_places=2)             # 设备报警阈值
    alert = models.BooleanField()                 # 设备是否报警
    sw = models.BooleanField()                # 设备开关
    onoff = models.CharField(max_length=10)   # 设备开关按钮显示


class History(models.Model):
    user = models.CharField(max_length=50)  # 设备所属用户
    identifier = models.CharField(max_length=20)  # 设备编号
    name = models.CharField(max_length=20)  # 设备名称
    physicalquantity = models.DecimalField(max_digits=4, decimal_places=2)  # 设备测得的物理量，如何设置
    updatetime = models.DateTimeField(auto_now=True)  # 设备最近更新时间
    alertline = models.DecimalField(max_digits=4, decimal_places=2)  # 设备报警阈值
    alert = models.BooleanField()  # 设备是否报警
    sw = models.BooleanField()  # 设备开关
    onoff = models.CharField(max_length=10)
