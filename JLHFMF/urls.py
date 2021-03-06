"""JLHFMF URL Configuration

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
from api.views import *

urlpatterns = [
    # Só é útil se tiver banco de dados ou sistema de autenticação
    path('admin/', admin.site.urls),
    path('login/', loginpage, name='login-page'),
    path('logout/', logout, name='logout'),
    path('', home, name='home'),
    path('retorna1/', return1, name='retorna_1'),
    path('retorna2/', return2, name='retorna_2'),
    path('upload/', simple_upload, name='upload'),
]
