# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from first_app.models import Topic,Webpage,AccessRecord,Users

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(Users)
