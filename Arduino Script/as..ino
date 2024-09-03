#define TRIGGER_PIN 7   // Trigger pin for ultrasonic sensor
#define ECHO_PIN 6      // Echo pin for ultrasonic sensor
#define LED_PIN 8       // LED pin

bool sosMode = false;   // LED blinking control
int currentState = 0;   // To track the current "yes" or "no" state

void setup() {
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Check for serial input (sos/stop command)
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    if (command == "sos") {
      sosMode = true;
    } else if (command == "stop") {
      sosMode = false;
      digitalWrite(LED_PIN, LOW);  // Turn off LED immediately
    }
  }

  // Handle LED blinking if in sos mode
  if (sosMode) {
    digitalWrite(LED_PIN, HIGH);
    delay(500);
    digitalWrite(LED_PIN, LOW);
    delay(500);
  } else {
    // Measure distance using the ultrasonic sensor
    long duration, distance;
    digitalWrite(TRIGGER_PIN, LOW);  
    delayMicroseconds(2);
    digitalWrite(TRIGGER_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_PIN, LOW);
    duration = pulseIn(ECHO_PIN, HIGH);
    distance = (duration / 2) / 29.1;

    // Determine and print the correct message based on the distance
    if (distance <= 20 && currentState != 1) {
      Serial.println("yes");
      currentState = 1;
    } else if (distance > 20 && distance <= 50 && currentState != 2) {
      Serial.println("no");
      currentState = 2;
    } else if (distance > 50 && currentState != 0) {
      currentState = 0;
    }
  }

  delay(100);  // Small delay to prevent excessive processing
}
