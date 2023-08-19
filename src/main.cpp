#include <Arduino.h>

#define TRIGGER_PIN 9

enum class Command : char { Trigger = 'T', Heartbeat = 'H', ACK = 'A' };

struct Packet {
  Command command;
};

void handleTrigger();

void setup() {
  pinMode(TRIGGER_PIN, OUTPUT);
  digitalWrite(TRIGGER_PIN, LOW);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() < (int)sizeof(Packet)) {
    return;
  }

  // Read packet
  Packet packet;
  Serial.readBytes((uint8_t *)&packet, sizeof(Packet));

  // Generate response
  Packet resp;
  switch (packet.command) {
  case Command::Trigger:
    handleTrigger();
    resp.command = Command::ACK;
    break;

  case Command::Heartbeat:
    resp.command = Command::ACK;
    break;

  default:
    return;
  }

  // Send response
  Serial.write((uint8_t *)&resp, sizeof(Packet));
}

void handleTrigger() {
  delay(500);
  digitalWrite(TRIGGER_PIN, HIGH);
  delay(2000);
  digitalWrite(TRIGGER_PIN, LOW);
  delay(500);
}
