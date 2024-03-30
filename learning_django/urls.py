"""
URL configuration for learning_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from learning_django import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('add_task',views.add_task,name='add_task'),
    path('completed_task',views.completed_task,name='completed_task'),
    path('deleted_task/<int:task_id>',views.deleted_task,name='deleted_task'),
    path('remaining_task',views.remaining_task,name='remaining_task'),
    path('task_detail/<int:task_id>',views.task_detail,name='task_detail'),
    path('remove_task/<int:task_id>',views.remove_task,name='remove_task'),
    path('toggle_completed/<int:task_id>',views.toggle_completed,name='toggle_completed'),
    
]                  
