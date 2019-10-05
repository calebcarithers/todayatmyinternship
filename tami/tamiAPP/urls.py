"""tami URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from .views import submit_page, home_page, new_home_page, detail_page, login_page



urlpatterns = [
    path('', home_page, name="home"),
    path('company/<str:company>', detail_page, name="detail"),
    path('new/', new_home_page, name="new"),
    path('new/company/<str:company>', detail_page, name="detail"),
    path('top/', home_page, name="home"),
    path('top/company/<str:company>', detail_page, name="detail"),
    path('submit/', submit_page, name="submit"),
    path('login/', login_page, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social"))
]