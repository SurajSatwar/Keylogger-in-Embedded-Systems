const int solenoidPin = 13;  // Pin connected to the solenoid

void setup() {
  pinMode(solenoidPin, OUTPUT);
  Serial.begin(9600);
  delay(1000);  // Small delay to ensure serial connection is stable
  Serial.println("Arduino is ready");
}

void loop() {
  if (Serial.available() > 0) {
    String password = Serial.readStringUntil('\n');
    Serial.print("Received password: ");
    Serial.println(password);
    if (password == "123456") {
      Serial.println("Password correct. Unlocking solenoid.");
      digitalWrite(solenoidPin, HIGH);  // Unlock solenoid
      delay(5000);  // Keep it unlocked for 5 seconds
      digitalWrite(solenoidPin, LOW);   // Lock solenoid
      Serial.println("Solenoid locked.");
    } else {
      Serial.println("Incorrect password.");
    }
  }
}
