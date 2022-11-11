import serial



arduino = serial.Serial("COM8",9600)
while True:
    datos="18"
    str(datos)
    arduino.write(datos.encode("ascii"))
    a=input("Desea continuar?")
    if(a.upper()!="S"):
        break
    #arduino.close()