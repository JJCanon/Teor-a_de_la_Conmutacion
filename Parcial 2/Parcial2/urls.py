"""Parcial2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Parcial2.views import mainMenu,Color1,Color2,Color3,Color4,Color5,Color6,Color7,Color8,Color9,Color10,Color11,Color12,Color13,Color14,Color15,Color16,Color17,Color18,Color19,Color20

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainMenu/',mainMenu),
    path('mainMenu/Color1On', Color1),
    path('mainMenu/Color2On', Color2),
    path('mainMenu/Color3On', Color3),
    path('mainMenu/Color4On', Color4),
    path('mainMenu/Color5On', Color5),
    path('mainMenu/Color6On', Color6),
    path('mainMenu/Color7On', Color7),
    path('mainMenu/Color8On', Color8),
    path('mainMenu/Color9On', Color9),
    path('mainMenu/Color10On', Color10),
    path('mainMenu/Color11On', Color11),
    path('mainMenu/Color12On', Color12),
    path('mainMenu/Color13On', Color13),
    path('mainMenu/Color14On', Color14),
    path('mainMenu/Color15On', Color15),
    path('mainMenu/Color16On', Color16),
    path('mainMenu/Color17On', Color17),
    path('mainMenu/Color18On', Color18),
    path('mainMenu/Color19On', Color19),
    path('mainMenu/Color20On', Color20),
    path('mainMenu/ColorOff',mainMenu)
]
