char a;  
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  pinMode(13,1);
  digitalWrite(13,0);
}

void loop() {
  if(Serial.available()){
    a=Serial.read();
        if(a=='1'){
  digitalWrite(13,1);
    }
  else digitalWrite(13,0);
  }
}
