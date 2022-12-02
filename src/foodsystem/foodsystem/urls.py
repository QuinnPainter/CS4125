"""foodsystem URL Configuration

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
from django.urls import path
from django.shortcuts import redirect

import foodsystem_app.views.menu
import foodsystem_app.views.payment
import foodsystem_app.views.login_register

def homepage(request):
	return redirect("login")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('menu', foodsystem_app.views.menu.MenuView.view_menu,name='menu'),
    path('add_to_order/<int:id>/', foodsystem_app.views.menu.MenuView.add_to_order, name='add_to_order'),
    path('remove_from_order/<int:id>/', foodsystem_app.views.menu.MenuView.remove_from_order, name='remove_from_order'),
    path("register", foodsystem_app.views.login_register.register_request, name="register"),
    path("login", foodsystem_app.views.login_register.login_request, name="login")
]
