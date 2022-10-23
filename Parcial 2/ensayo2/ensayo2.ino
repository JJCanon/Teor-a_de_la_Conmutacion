void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  float s1 = analogRead(A0);
  //float s2 = analogRead(A0)*0.5;
  // print out the value you read:
  //Serial.print(s1);
  //Serial.print(",");
  Serial.println(s1);
  delay(200);
}// delay para estabilidad
