#define RED 2
#define YELLOW 3
#define GREEN 4

void setup() {
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(GREEN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {  // Check if data is available
    String receivedData = Serial.readStringUntil('\n');  // Read incoming data
    int signal_time = receivedData.toInt();  // Convert string to integer

    Serial.print("Received signal time: ");
    Serial.println(signal_time);

    // Green signal
    digitalWrite(GREEN, HIGH);
    digitalWrite(RED, LOW);
    digitalWrite(YELLOW, LOW);
    delay(signal_time * 1000);  // Keep green for received time

    // Yellow signal
    digitalWrite(GREEN, LOW);
    digitalWrite(YELLOW, HIGH);
    delay(2000);

    // Red signal
    digitalWrite(YELLOW, LOW);
    digitalWrite(RED, HIGH);
    delay(5000);
  }
}
