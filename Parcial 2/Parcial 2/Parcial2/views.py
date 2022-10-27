from turtle import color
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.template import loader
import serial

arduino = serial.Serial("COM8",9600)
#Variables
red=0
green=0
blue=0
color1=0
color2=0
color3=0
color4=0
color5=0
color6=0
color7=0
color8=0
color9=0
color10=0
color11=0
color12=0
color13=0
color14=0
color15=0
color16=0
color17=0
color18=0
color19=0
color20=0
 
def mainMenu(request):
    
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color1(request):
    color1=1
    enviarValor(1)
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
    
def enviarValor(a):
    arduino.write(2)
    print(2)