"""Proyecto1 URL Configuration

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
from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.contrib.auth import login
from gestionEmpleados import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestionEmpleados/', include('gestionEmpleados.urls')),
    url(r'^$',LoginView.as_view(template_name='login.html'),name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('logout/',logout_then_login,name='logout'),
    path('registroE/', views.registroE),
    path('registroEm/', views.registroEm),
    path('registroDep/', views.registroDep),
    path('reporteE/', views.rep_empe),#rep_d
    path('reporteDep/', views.rep_d),
    path('reporteEmple/', views.re_nombre),
    
]
