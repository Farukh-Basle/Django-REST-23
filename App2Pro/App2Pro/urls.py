"""App2Pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from App2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.regiser_view),
    path('login/',views.get_token),
    path('getallemps/',views.getAllEmps),
    path('getempbyid/<int:pk>/',views.get_emp_by_id),
    path('gdel_empbyid/<int:pk>/',views.del_emp_by_id),
    path('create/',views.createView),
    path('update/<int:pk>/',views.UpdateView),
]
