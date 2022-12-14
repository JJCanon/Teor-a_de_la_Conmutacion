
from .forms import *
from pymongo import MongoClient
from django.shortcuts import render, redirect
from django.http import HttpResponse
import serial
import time

#Variables Mongo
Cliente = MongoClient('localhost')

db = Cliente['Conmutacion']

Users = db['Users']
Houses = db['Houses'] 
#variables para Arduino
arduino = serial.Serial("COM8",9600)
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

#Formulario de Inicio de Sesión
def signIn(request):
    return render(request,'signIn.html')

def cerrarSesion(request):
    dato="7"
    arduino.write(dato.encode('ascii'))
    time.sleep(2)
    return redirect('/signIn/')

#Menú Principal
def mainMenu(request):
    form = pasar_dato()
    name = str(request.POST["nameUser"])
    password= str(request.POST["pass"])
    exist=False
    for p in Users.find():
        if(p['Name']==name and p['Password']==password):
            exist=True
    if exist:         
        Cliente=Users.find_one({"Name":name,"Password":password})
        Casa=Houses.find_one({"Name":Cliente['House']})
        house="5"
        arduino.write(house.encode('ascii'))
        time.sleep(2)
        house=Casa['id']
        house=str(house)
        arduino.write(house.encode('ascii'))
        time.sleep(5)
        context ={"nombreCliente": Cliente['Name'], "formulario":form,"id":house}
        return render(request,'mainMenu.html',context)
    else:     
        return render(request,'error.html')
    
def mainMenu2(request):
    house="21"
    arduino.write(house.encode('ascii'))
    time.sleep(2)
    return render(request,'mainMenu.html')

#Formulario de Registro
def signUp(request):
    return render(request,'signUp.html')

#Nuevo Usuario
def registro(request):
    form=pasar_dato()
    name=str(request.POST["nameUser"])
    password=str(request.POST["pass"])
    nameHouse=str(request.POST["nameHouse"])
    idHouse=str(request.POST["idHouse"])
    existh=False
    for h in Houses.find():
        if(h['Name']==nameHouse and h['id']==idHouse):
            existh=True
    existc=True
    for c in Users.find():
        if(c['Name'] == name):
            existc=False
    if (existh and existc):
        Users.insert_one({"Name":name, "Password":password,"House": nameHouse})
        context ={"nombreCliente": name}
        return render(request,'RegistroExitoso.html',context)
    else:
        if not existc:
            return render(request,'errorH.html',{"Cliente": 1 })
        else:
            return render(request,'errorH.html',{"Cliente": 0 })

def sala(request):
    lugarCasa="21"
    arduino.write(lugarCasa.encode("ascii"))
    time.sleep(2)
    lugarCasa="1"
    arduino.write(lugarCasa.encode('ascii'))
    time.sleep(3)
    return tablaColores(request)
def cocina(request):
    lugarCasa="21"
    arduino.write(lugarCasa.encode("ascii"))
    time.sleep(2)
    lugarCasa="2"
    arduino.write(lugarCasa.encode("ascii"))
    time.sleep(2)
    return tablaColores(request)    
def cuarto(request):
    lugarCasa="21"
    arduino.write(lugarCasa.encode("ascii"))
    time.sleep(2)
    lugarCasa="3"
    arduino.write(lugarCasa.encode("ascii"))
    time.sleep(2)
    return tablaColores(request) 


#EncenderColores
def tablaColores(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    

    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def apagar(request):
    datos="0"
    str(datos)
    arduino.write(datos.encode("ascii"))
    return redirect('/signIn/mainMenu/tablaColores/')
  
def Color1(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color1=1
    if True:
        datos="1"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color2(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color2=1
    if True:
        datos="2"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color3(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color3=1
    if True:
        datos="3"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color4(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color4=1
    if True:
        datos="4"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color5(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color5=1
    if True:
        datos="5"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color6(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color6=1
    if True:
        datos="6"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color7(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color7=1
    if True:
        datos="7"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color8(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color8=1
    if True:
        datos="8"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color9(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color9=1
    if True:
        datos="9"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color10(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color10=1
    if True:
        datos="10"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color11(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color11=1
    if True:
        datos="11"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color12(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color12=1
    if True:
        datos="12"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color13(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color13=1
    if True:
        datos="13"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color14(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color14=1
    if True:
        datos="14"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color15(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color15=1
    if True:
        datos="15"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color16(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color16=1
    if True:
        datos="16"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color17(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color17=1
    if True:
        datos="17"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color18(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color18=1
    if True:
        datos="18"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color19(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color19=1
    if True:
        datos="19"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
def Color20(request):
    valor = str(arduino.readline())
    valor1=valor[2:5]
    palabra=""
    if(int(valor1)==100):
        palabra="encendido"
    else:
        palabra="apagado"
    
    color20=1
    if True:
        datos="20"
        str(datos)
        arduino.write(datos.encode("ascii"))
    return render(request, "tablaColores.html",{"Red": red,"Green": green, "Blue":blue,
                                            "Color1": color1,"Color2": color2,"Color3": color3,"Color4": color4,"Color5": color5,
                                            "Color6": color6,"Color7": color7,"Color8": color8,"Color9": color9,"Color10": color10,
                                            "Color11": color11,"Color12": color12,"Color13": color13,"Color14": color14,"Color15": color15,
                                            "Color16": color16,"Color17": color17,"Color18": color18,"Color19": color19,"Color20": color20,"valor":palabra})
             