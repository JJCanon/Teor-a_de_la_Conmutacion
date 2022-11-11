from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.template import loader
import serial


#Variables
#arduino = serial.Serial("COM8",9600)

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
    if True:
        datos="0"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color1(request):
    color1=1
    if True:
        datos="1"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color2(request):
    color2=1
    if True:
        datos="2"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color3(request):
    color3=1
    if True:
        datos="3"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color4(request):
    color4=1
    if True:
        datos="4"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color5(request):
    color5=1
    if True:
        datos="5"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color6(request):
    color6=1
    if True:
        datos="6"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color7(request):
    color7=1
    if True:
        datos="7"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color8(request):
    color8=1
    if True:
        datos="8"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color9(request):
    color9=1
    if True:
        datos="9"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color10(request):
    color10=1
    if True:
        datos="10"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color11(request):
    color11=1
    if True:
        datos="11"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color12(request):
    color12=1
    if True:
        datos="12"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color13(request):
    color13=1
    if True:
        datos="13"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color14(request):
    color14=1
    if True:
        datos="14"
        str(datos)
       # arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color15(request):
    color15=1
    if True:
        datos="15"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color16(request):
    color16=1
    if True:
        datos="16"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color17(request):
    color17=1
    if True:
        datos="17"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color18(request):
    color18=1
    if True:
        datos="18"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color19(request):
    color19=1
    if True:
        datos="19"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
def Color20(request):
    color20=1
    if True:
        datos="20"
        str(datos)
        #arduino.write(datos.encode("ascii"))
    return render(request, "MainMenu.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20})
    