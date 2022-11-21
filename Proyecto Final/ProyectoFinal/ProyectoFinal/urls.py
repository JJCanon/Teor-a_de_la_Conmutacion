"""ProyectoFinal URL Configuration

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
from ProyectoFinal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signIn/', signIn),
    path('cerrarSesion/',cerrarSesion),
    path('signIn/mainMenu', mainMenu),
    path('signIn/mainMenu2',mainMenu2),
    path('signUp/',signUp),
    path('signUp/registro', registro),
    path('signIn/mainMenu/tablaColores/',tablaColores),
    path('signIn/mainMenu/tablaColores/Color1On', Color1),
    path('signIn/mainMenu/tablaColores/Color2On', Color2),
    path('signIn/mainMenu/tablaColores/Color3On', Color3),
    path('signIn/mainMenu/tablaColores/Color4On', Color4),
    path('signIn/mainMenu/tablaColores/Color5On', Color5),
    path('signIn/mainMenu/tablaColores/Color6On', Color6),
    path('signIn/mainMenu/tablaColores/Color7On', Color7),
    path('signIn/mainMenu/tablaColores/Color8On', Color8),
    path('signIn/mainMenu/tablaColores/Color9On', Color9),
    path('signIn/mainMenu/tablaColores/Color10On', Color10),
    path('signIn/mainMenu/tablaColores/Color11On', Color11),
    path('signIn/mainMenu/tablaColores/Color12On', Color12),
    path('signIn/mainMenu/tablaColores/Color13On', Color13),
    path('signIn/mainMenu/tablaColores/Color14On', Color14),
    path('signIn/mainMenu/tablaColores/Color15On', Color15),
    path('signIn/mainMenu/tablaColores/Color16On', Color16),
    path('signIn/mainMenu/tablaColores/Color17On', Color17),
    path('signIn/mainMenu/tablaColores/Color18On', Color18),
    path('signIn/mainMenu/tablaColores/Color19On', Color19),
    path('signIn/mainMenu/tablaColores/Color20On', Color20),
    path('signIn/mainMenu/tablaColores/ColorOff',apagar),
    path('signIn/mainMenu/tablaColores/sala',sala),
    path('signIn/mainMenu/tablaColores/cocina',cocina),
    path('signIn/mainMenu/tablaColores/cuarto',cuarto),
    
]
