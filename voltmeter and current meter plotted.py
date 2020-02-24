const int analogPin = A6;    // pin that the sensor is attached to
const int ledPin = 2;       // pin that the LED is attached to
const int threshold = 400;

void setup() {
 pinMode(ledPin, OUTPUT);
 Serial.begin(9600);
}

void loop() {
  int controlValue = analogRead(A6);
  if (controlValue > threshold) {
    digitalWrite(ledPin, HIGH);
  } else {
    digitalWrite(ledPin, LOW);
  }
  int sensor1Value = analogRead(A1);
  int sensor2Value = analogRead(A2);
  
  
float sensor1 = sensor1Value * (24.0 / 1023.0);
float sensor2 = sensor2Value * (1.69 /1023.0);
  Serial.print(sensor1);
  Serial.print(" ");
  Serial.println(sensor2);
  
  



delay(50);
}
