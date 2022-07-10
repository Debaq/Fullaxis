int inByte = 0;
bool connect_state = false;
bool transmit = true;

int repeat_receptor = 9;
unsigned long t = 0;

void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);

}

void loop() {

  

  while (connect_state == false) {
    Serial.println("esperando conexión");
    digitalWrite(2, LOW);
    if (Serial.available() > 0) {
      inByte = Serial.read();
      delay(10);
      if (inByte == 51) {
      }
      digitalWrite(2, LOW);
      connect_state = true;
      delay(10);
      Serial.println("Soy Tu receptor t:10");
      break;
    }
    delay(100);
    digitalWrite(2, HIGH);
    delay(100);
  }
  
  if (connect_state == true && repeat_receptor > 0) {
    repeat_receptor = repeat_receptor - 1;
    Serial.print("Soy Tu receptor t:");
    Serial.println(repeat_receptor);
  }
  else {
    if (transmit == true) {
      unsigned long dt = millis() - t;
      
      int x = random(-10 , 300);
      int y = random(-150, 150);
      int z = random(100);
      int batt = random(300 , 370);
      Serial.print(x);
      Serial.print(",");
      Serial.print(y);
      Serial.print(",");
      Serial.print(z);
      Serial.print(",");
      Serial.print(dt);
      Serial.print(",");
      Serial.println(batt);
      delay(10);
      if (Serial.available() > 0) {
        inByte = Serial.read();
        if (inByte == 52) {
          t = millis();
        }
        if (inByte == 53) {
          transmit = false;
        }
      }
    }
    else {
      if (Serial.available() > 0) {
        inByte = Serial.read();
        if (inByte == 53) {
          transmit = true;
        }
      }

    }
  }

}
