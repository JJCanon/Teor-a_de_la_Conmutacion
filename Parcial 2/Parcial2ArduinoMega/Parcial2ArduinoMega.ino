#include <Wire.h>
#define red1 A0
#define green1 A1
#define blue1 A2
#define green2 A4
#define red2 A5
#define blue2 A6
#define red3 2
#define green3 3
#define blue3 4

/*void orden();
void color(int a, int b, int c);
void apagar();*/

void setup() {

  pinMode(red1, OUTPUT); pinMode(green1, OUTPUT); pinMode(blue1, OUTPUT);
  pinMode(red2, OUTPUT); pinMode(green2, OUTPUT); pinMode(blue2, OUTPUT);
  pinMode(red3, OUTPUT); pinMode(green3, OUTPUT); pinMode(blue3, OUTPUT);
  analogWrite(red1, 0); analogWrite(green1, 0); analogWrite(blue1, 0);
  analogWrite(red2, 0); analogWrite(green2, 0); analogWrite(blue2, 0);
  analogWrite(red3, 0); analogWrite(green3, 0); analogWrite(blue3, 0);
  Serial.begin(9600);
  Wire.begin(0x01); // esclavo
  Wire.onReceive(orden);
}

void loop() {
  /*analogWrite(red1,135);analogWrite(green1,65);analogWrite(blue1,137);
    analogWrite(red2,135);analogWrite(green2,65);analogWrite(blue2,137);
    analogWrite(red3,165);analogWrite(green3,65);analogWrite(blue3,137);*/
}

void orden() {
  while (Wire.available())
  {

    char x = Wire.read();
    Serial.println(x);
    /*if (x != 1) {
      color(100, 200, 150);
      Serial.print("hola");
    }
    else
    {
      Serial.print("no");
      apagar();
    }*/
  }
  //Serial.println(cadena);
}

void color(int a, int b, int c)
{
  analogWrite(red1, a); analogWrite(green1, b); analogWrite(blue1, c);
  analogWrite(red2, a); analogWrite(green2, b); analogWrite(blue2, c);
  analogWrite(red3, a); analogWrite(green3, b); analogWrite(blue3, c);
  delay(5000);
}

void apagar()
{
  analogWrite(red1, 0); analogWrite(green1, 0); analogWrite(blue1, 0);
  analogWrite(red2, 0); analogWrite(green2, 0); analogWrite(blue2, 0);
  analogWrite(red3, 0); analogWrite(green3, 0); analogWrite(blue3, 0);
}
