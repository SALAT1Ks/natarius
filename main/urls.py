from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index),
    path('', views.index),
    path('about', views.about),
    path('tariffy', views.tariffy),
    path('required_documents', views.required_documents),
    path('contacts', views.contacts),
]