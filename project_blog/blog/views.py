# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse('welcome to django learning !')
    return render(request,'index.html')
    
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    return HttpResponse(str(int(a)+int(b)))

def add2(request,a,b):
    return HttpResponse(str(int(a)+int(b)))
    

