from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return revrse('mtweb:index')
    # return redirect(request,'index.html')
    return HttpResponse("aaaaa")