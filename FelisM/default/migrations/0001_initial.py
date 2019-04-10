# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-08 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('identifier', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('physicalquantity', models.DecimalField(decimal_places=2, max_digits=4)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('alertline', models.DecimalField(decimal_places=2, max_digits=4)),
                ('alert', models.BooleanField()),
                ('sw', models.BooleanField()),
                ('onoff', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('identifier', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('physicalquantity', models.DecimalField(decimal_places=2, max_digits=4)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('alertline', models.DecimalField(decimal_places=2, max_digits=4)),
                ('alert', models.BooleanField()),
                ('sw', models.BooleanField()),
                ('onoff', models.CharField(max_length=10)),
            ],
        ),
    ]