//includes
#include <Wire.h>

//defines

//variables
int valor;
String valorS;

void setup() {
  Wire.begin();
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()) {
    valorS=Serial.readString();
    valor=valorS.toInt();
    Wire.beginTransmission(1);
    Serial.println(valor);
    Wire.write(valor);
    Wire.endTransmission();
  }

}
