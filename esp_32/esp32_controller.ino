#include <WiFi.h>
#include <AccelStepper.h>

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";

WiFiServer server(1234);

// Motor 1 (Base)
AccelStepper baseMotor(AccelStepper::FULL4WIRE, 14, 26, 27, 25);

// Motor 2 (Arm)
AccelStepper armMotor(AccelStepper::FULL4WIRE, 33, 18, 32, 19);

int targetX = 0;
int targetY = 0;

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  Serial.println(WiFi.localIP());
  server.begin();

  baseMotor.setMaxSpeed(400);
  baseMotor.setAcceleration(200);

  armMotor.setMaxSpeed(400);
  armMotor.setAcceleration(200);
}

void loop() {
  WiFiClient client = server.available();

  if (client) {
    String data = client.readStringUntil('\\n');

    int comma = data.indexOf(',');
    targetX = data.substring(0, comma).toInt();
    targetY = data.substring(comma + 1).toInt();
  }

  int stepsX = map(targetX, 0, 180, 0, 2048);
  int stepsY = map(targetY, 0, 180, 0, 2048);

  baseMotor.moveTo(stepsX);
  armMotor.moveTo(stepsY);

  baseMotor.run();
  armMotor.run();
}