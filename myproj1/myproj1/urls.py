"""
URL configuration for myproj1 project.

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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mohit/',views.myfirstprogram),
    path('add/<int:a>/<int:b>/',views.add),
    path('minus/<int:a>/<int:b>/',views.minus),
    path('name/<str:n>/',views.name),
    path('checkprime/<int:n>/',views.prime_notprime),
    path('checkevenodd/<int:n>/',views.even_odd),
    path('index/',views.index),
    path('home/<int:n>/',views.Home)

]
