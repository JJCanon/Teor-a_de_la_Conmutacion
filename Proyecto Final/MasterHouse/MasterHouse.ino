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
void setup() {
  Wire.begin();
  Serial.begin(9600);
  house = false;
  housePart = false;
}

void loop() {
  if (house)
  {
    if (housePart)
    {
      if (Serial.available()) {

        valorS = Serial.readString();
        valor = valorS.toInt();
        if (valor <= 20) {
          Wire.beginTransmission(casa);
          Serial.print(casa);
          Serial.print(" ");
          Serial.println(valor);
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
          Serial.print(casa);
          Serial.print(" ");
          Serial.println(a);
          Wire.write(a);
          Wire.endTransmission();
          Serial.print("Habitacion Asignada ");
          Serial.println(habitacion);
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
        Serial.print("casa asignada ");
        Serial.println(casa);
      }
    }
  }
}
