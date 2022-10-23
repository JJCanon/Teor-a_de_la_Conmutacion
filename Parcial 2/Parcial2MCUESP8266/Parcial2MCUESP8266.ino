//Librerias y Defines
#include <Wire.h>
#define morado 12
#define celeste 14

//variables

int red;
String a;
int green;
String b;
int blue;
String c;
String cadena;
void setup() {
  Serial.begin(9600);
  Wire.begin(); // maestro
  pinMode(morado, INPUT);
  pinMode(celeste, INPUT);
}


void loop() {
  Wire.beginTransmission(1);
  Wire.write("hola");
  Serial.println("color");
  Wire.endTransmission();

}
