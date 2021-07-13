"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers

import todo.views
from main.views import index

router = routers.DefaultRouter()
router.register('todo', todo.views.TaskAPI, basename='todo_api')
router.register('todo_add', todo.views.TaskAddAPI, basename='todo_add_api')
router.register('todo_del', todo.views.TaskDelAPI, basename='todo_del_api')

urlpatterns = [
    path('', index, name='main'),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('todo/', todo.views.task, name='todo'),
    path('accounts/', include('django.contrib.auth.urls')),
]
