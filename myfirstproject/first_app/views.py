# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Webpage,Topic
from . import forms

# Create your views here.
def index(request):
    """text=""""""<em>hello world</em>""""""
    return HttpResponse("<em>hello world</em>")"""
    web_list= AccessRecord.objects.order_by("date")
    date_dict={"access_record":web_list}
    return render(request,"first_app/index.html",context=date_dict)

def help(request):
    help_dic={"help_request":"HELP PAGE"}
    return render(request ,"first_app/help.html",context=help_dic)

def form_page_view(request):
    form=forms.FormPage()

    if request.method =='POST':
        form= forms.FormPage(request.POST)

        if form.is_valid():
            print("Validation Success!!!")
            print("Name: "+form.cleaned_data["name"])
            print("Email: "+form.cleaned_data["email"])
            print("Text: "+form.cleaned_data["text"])





    return render(request, "first_app/form.html",{"form":form})



def users(request):
    form=forms.NewUserForm()

    if request.method=='POST':
        form=forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("Validation Successful!!!")
        else:
            print("Validation error!!!")

    return render(request,"first_app/users.html",{"form":form})

def base_template(request):
    return render(request,"first_app/base.html",{})

def test_template(request):
    my_dict={"test":"hello world"}
    return render(request,"first_app/test1.html",context=my_dict)
