from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views



urlpatterns = [
                  path("", views.crm_index, name="crm home")
              ]
