# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

class Topic(models.Model):
    top_name=models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    category=models.ForeignKey(Topic)
    name=models.CharField(max_length=264, unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage)
    date=models.DateField()

    def __str__(self):
        return str(self.date)

class Users(models.Model):
    first=models.CharField(max_length=264)
    last=models.CharField(max_length=264)
    email=models.EmailField()

    def __str__(self):
        return self.first
