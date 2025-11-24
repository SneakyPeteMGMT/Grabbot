// Minimal Arduino serial stub for Grabbot
// Zweck: empfängt einfache newline-terminated Befehle wie "MOVE JOINT1 90"
// und antwortet mit "OK" oder "ERR"

void setup() {
  Serial.begin(115200);
  // initial setup: Pins, PWM, etc.
  Serial.println("Grabbot Arduino ready");
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();
    if (cmd.length() == 0) return;

    // einfache Echo-Logik (Ersetzen durch echte Steuerbefehle)
    Serial.print("RECV: ");
    Serial.println(cmd);
    Serial.println("OK");
  }
}