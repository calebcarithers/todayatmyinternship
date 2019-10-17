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

from .views import submit_page, home_page, home_new_page, detail_new_page, detail_page, login_page



urlpatterns = [
    path('admin/', admin.site.urls),

    # home page urls
    path('', home_page, name="home"),
    path('new/', home_new_page, name="new"),
    path('top/', home_page, name="home"),
    path('new/<str:company>/top', detail_page, name="detail_company_top"),
    path('top/<str:company>/top', detail_page, name="detail_company_top"),

    # company page urls
    path('company/<str:company>', detail_page, name="detail"),
    # path('<str:company>', detail_top_page, name="detail"),
    path('<str:company>/top', detail_page, name="detail_top"),
    path('<str:company>/new', detail_new_page, name="detail_new"),

    # menu bar urls
    path('submit/', submit_page, name="submit"),
    path('login/', login_page, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    # social-auth urls
    path('social-auth/', include('social_django.urls', namespace="social")),

    # auth urls
    path('accounts/', include('django.contrib.auth.urls'))
]