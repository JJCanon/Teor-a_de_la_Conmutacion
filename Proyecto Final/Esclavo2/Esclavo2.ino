//includes
#include <Wire.h>
//defines
#define red1 A1
#define green1 A0
#define blue1 A2
#define red2 A5
#define green2 A4
#define blue2 A6
#define red3 3
#define green3 2
#define blue3 4

//funciones
void dato();
void color(int a, int b, int c);
void apagar();

//variables
int Acuamarine[] = {127, 255, 212}; int Blue[] = {0, 0, 255}; int BlueViolet[] = {138, 43, 226}; int Brown[] = {165, 42, 42};
int Chartreuse[] = {127, 255, 0}; int Coral[] = {255, 127, 80}; int Crimson[] = {220, 20, 60}; int DarkGreen[] = {0, 150, 0};
int Indigo[] = {105, 50, 53}; int LightPink[] = {255, 182, 193}; int Lightslategrey[] = {119, 136, 153}; int Green[] = {0, 255, 0};
int Orangered[] = {255, 69, 0}; int RoyalBlue[] = {65, 105, 255}; int Violet[] = {238, 130, 238}; int Yellow[] = {255, 255, 0};
int White[] = {245, 245, 245}; int Red[] = {255, 0, 0}; int GreenYellow[] = {173, 255, 47}; int Khaki[] = {189, 183, 107};
bool sala;
bool cocina;
bool room;
void setup() {
  Serial.begin(9600);
  Wire.begin(2);
  Wire.onReceive(dato);
  pinMode(red1, OUTPUT); pinMode(green1, OUTPUT); pinMode(blue1, OUTPUT);
  pinMode(red2, OUTPUT); pinMode(green2, OUTPUT); pinMode(blue2, OUTPUT);
  pinMode(red3, OUTPUT); pinMode(green3, OUTPUT); pinMode(blue3, OUTPUT);
  analogWrite(red1, 0); analogWrite(green1, 0); analogWrite(blue1, 0);
  analogWrite(red2, 0); analogWrite(green2, 0); analogWrite(blue2, 0);
  analogWrite(red3, 0); analogWrite(green3, 0); analogWrite(blue3, 0);

  pinMode(22, OUTPUT);
}

void loop() {
}

void dato() {

  if (Wire.available())
  {
    int dato = Wire.read();
    Serial.println(dato);
    switch (dato) {
      case 0:
        color(0, 0, 0);
        break;
      case 1:
        color(Acuamarine[0], Acuamarine[1], Acuamarine[2]);
        break;
      case 2:
        color(Blue[0], Blue[1], Blue[2]);
        break;
      case 3:
        color(BlueViolet[0], BlueViolet[1], BlueViolet[2]);
        break;
      case 4:
        color(Brown[0], Brown[1], Brown[2]);
        break;
      case 5:
        color(Chartreuse[0], Chartreuse[1], Chartreuse[2]);
        break;
      case 6:
        color(Coral[0], Coral[1], Coral[2]);
        break;
      case 7:
        color(Crimson[0], Crimson[1], Crimson[2]);
        break;
      case 8:
        color(DarkGreen[0], DarkGreen[1], DarkGreen[2]);
        break;
      case 9:
        color(Indigo[0], Indigo[1], Indigo[2]);
        break;
      case 10:
        color(LightPink[0], LightPink[1], LightPink[2]);
        break;
      case 11:
        color(Lightslategrey[0], Lightslategrey[1], Lightslategrey[2]);
        break;
      case 12:
        color(Green[0], Green[1], Green[2]);
        break;
      case 13:
        color(Orangered[0], Orangered[1], Orangered[2]);
        break;
      case 14:
        color(RoyalBlue[0], RoyalBlue[1], RoyalBlue[2]);
        break;
      case 15:
        color(Violet[0], Violet[1], Violet[2]);
        break;
      case 16:
        color(Yellow[0], Yellow[1], Yellow[2]);
        break;
      case 17:
        color(White[0], White[1], White[2]);
        break;
      case 18:
        color(Red[0], Red[1], Red[2]);
        break;
      case 19:
        color(GreenYellow[0], GreenYellow[1], GreenYellow[2]);
        break;
      case 20:
        color(Khaki[0], Khaki[1], Khaki[2]);
        break;
      case 21:
        sala = true;
        cocina = false;
        room = false;
        break;
      case 22:
        sala = false;
        cocina = true;
        room = false;
        break;
      case 23:
        sala = false;
        cocina = false;
        room = true;
        break;
      default:
        //apagar();
        break;
    }
  }
}

void color(int a, int b, int c)
{
  if (sala) {
    analogWrite(red1, a); analogWrite(green1, b); analogWrite(blue1, c);
  }
  else if (cocina) {
    analogWrite(red2, a); analogWrite(green2, b); analogWrite(blue2, c);
  }
  else if (room) {
    analogWrite(red3, a); analogWrite(green3, b); analogWrite(blue3, c);
  }
  delay(1000);
}

void apagar()
{
  analogWrite(red1, 0); analogWrite(green1, 0); analogWrite(blue1, 0);
  analogWrite(red2, 0); analogWrite(green2, 0); analogWrite(blue2, 0);
  analogWrite(red3, 0); analogWrite(green3, 0); analogWrite(blue3, 0);
}
