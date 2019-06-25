"""travel URL Configuration

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
from app import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('user/create', views.create_user),
    path('travels', views.travels),
    path('login', views.login),
    path('logout', views.logout),
    path('travels/add', views.addtrip),
    path('create_trip', views.create_trip),
    path('join/<int:trip_id>', views.join),
    path('destination/<int:trip_id>', views.destination),

]
