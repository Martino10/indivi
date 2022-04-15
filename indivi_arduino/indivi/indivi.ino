#include "SevenSegmentTM1637.h"
const int DISPLAY_CLK = 2;
const int DISPLAY_DIO = 3;
int LDRstatus = 0;
const int LDR = A0;
String data;

SevenSegmentTM1637 display(DISPLAY_CLK, DISPLAY_DIO);

void setup() {
  
  Serial.begin(9600);
  pinMode(LDR, INPUT);
  display.begin();
  display.setBacklight(100);
  
}

void loop() {
  while (Serial.available()) {
    data = Serial.readStringUntil('\n');
  }
  display.clear();
  display.print(data);
  
  // LDR status
  LDRstatus = analogRead(LDR);
  Serial.println(LDRstatus);
  delay(1000);
}
