from django.contrib import admin
from django.urls import path, include
import main_app.views
from main_app import views

urlpatterns = [
    path('', views.index, name="main")
]
