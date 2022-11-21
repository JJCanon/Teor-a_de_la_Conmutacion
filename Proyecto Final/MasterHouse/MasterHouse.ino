//includes
#include <Wire.h>

//defines

//variables
int valor;
String valorS;
int casa;
int habitacion;
bool house;
bool housePart;
bool encendido = true;
bool apagado = false;
void setup() {
  Wire.begin();

  Serial.begin(9600);
  house = false;
  housePart = false;
  Serial.println("hola");
}

void loop() {
  if (house)
  {
    if (housePart)
    {
      Wire.requestFrom(1, 1);
      if (Wire.available()) {
        int c = Wire.read();
        if (c == 1)
        {
          if (encendido) {
            Serial.println(100);
            encendido = false;
          } else {
            apagado = true;
          }
        } else
        {
          if (apagado)
          {
            Serial.println(200);
            apagado = false;
          } else {
            encendido = true;
          }
        }
      }
      if (Serial.available()) {

        valorS = Serial.readString();
        valor = valorS.toInt();
        if (valor <= 20) {
          Wire.beginTransmission(casa);
          /*Serial.print(casa);
          Serial.print(" ");
          Serial.println(valor);*/
          Wire.write(valor);
          Wire.endTransmission();
        } else
        {
          housePart = false;
        }
      }
    }
    else
    {
      if (Serial.available())
      {
        valorS = Serial.readString();
        valor = valorS.toInt();
        if (valor > 3 && valor < 10)
        {
          house = false;
        } else if (valor < 4)
        {
          habitacion = valor;
          housePart = true;
          int a;
          switch (habitacion) {
            case 1:
              a = 21;
              break;
            case 2:
              a = 22;
              break;
            case 3:
              a = 23;
              break;
            case 21:
              housePart = false;
              break;
            default:
              break;
          }
          Wire.beginTransmission(casa);
          /*Serial.print(casa);
          Serial.print(" ");
          Serial.println(a);*/
          Wire.write(a);
          Wire.endTransmission();
          /*Serial.print("Habitacion Asignada ");
          Serial.println(habitacion);*/
        }
      }
    }
  } else {
    if (Serial.available())
    {
      valorS = Serial.readString();
      valor = valorS.toInt();
      casa = valor;
      if (casa < 4)
      {
        house = true;
        /*Serial.print("casa asignada ");
        Serial.println(casa);*/
      }
    }
  }
}
