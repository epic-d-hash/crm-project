from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader


def shcm_home(request):
    template = loader.get_template('shcm-home.html')
    return HttpResponse(template.render())


def recruiter_login(request):
    template = loader.get_template('Recruiter/login.html')
    return HttpResponse(template.render())


def employer_login(request):
    template = loader.get_template('Employer/login.html')
    return HttpResponse(template.render())


def admin_login(request):
    template = loader.get_template('Admin/login.html')
    return HttpResponse(template.render())


