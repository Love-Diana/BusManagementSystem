"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path
import data.views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',data.views.menu),
    path('enter/',data.views.enter),
    path("add_driver/",data.views.add_driver),
    path("add_fine/",data.views.add_fine),
    path("add_motor/",data.views.add_motor),
    path("select_fine/",data.views.select_fine),
    path("fine_count/",data.views.fine_count),
    path("select_drivers/",data.views.select_drivers),
]
