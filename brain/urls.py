from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView

from .views import Register

urlpatterns = [
    path('',  include('django.contrib.auth.urls')),
    path('registration/' , Register.as_view(),name='register')
]
