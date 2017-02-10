"""Shareback_PyServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from shareback_app import views

urlpatterns = [
   url(r'^admin/', admin.site.urls),
  url(r'^test/', views.test, name='test'),
   
     url(r'^test/upload/', views.test_upload, name='test_upload'),
   
   
     url(r'^feedback/get/', views.feedback_get, name='feedback_get'),
     url(r'^feedback/insert/', views.feedback_insert, name='feedback_insert'),
     url(r'^file/cp/', views.file_copy, name='cp'),
     url(r'^file/del/', views.file_delete, name='del'),
     url(r'^file/ls/', views.file_ls, name='ls'),
     url(r'^file/mkdir/', views.file_mkdir, name='mkdir'),
     url(r'^file/mv/', views.file_move, name='move'),
     url(r'^file/rename/', views.file_rename, name='rename'),
     url(r'^file/upload/', views.file_upload, name='upload'),
     url(r'^prev_sessions/', views.prev_sessions, name='prev_sessions'),
     url(r'^session/start/', views.start_sesssion, name='start_session'),

]