from django.shortcuts import render,redirect
from django.http import HttpResponse



def shcm_home(request):
    return HttpResponse("<h1> SCHM Home </h1>")
