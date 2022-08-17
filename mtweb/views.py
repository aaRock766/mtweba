from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return reverse('mtweb:index')
    return redirect(reverse('mtweb:index'))
    # return HttpResponse("aaaaa")
    # return render(request,'index.html')