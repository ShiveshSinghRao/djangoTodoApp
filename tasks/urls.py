# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('update_task/<str:pk>/',views.updateTask,name='update_task'),
]
