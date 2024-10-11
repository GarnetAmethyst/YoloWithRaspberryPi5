#include <Arduino.h>

int ledPin = 12;  // LED�� ����� �� ��ȣ

void setup() {
    pinMode(ledPin, OUTPUT);
    digitalWrite(ledPin, LOW);  // �ʱ� ���¿��� LED �������� ����
    Serial.begin(9600);  // �ø��� ��� ����
}

void loop() {
    if (Serial.available() > 0) {  // �ø��� �Է��� �ִ� ���
        char command = Serial.read();  // �ø��󿡼� ����� ����
        Serial.println(command);  // �����: ���ŵ� ��� ���
        
        if (command == '1') {
            digitalWrite(ledPin, HIGH);  // LED ON
            delay(500);  // 0.5�� ���
            digitalWrite(ledPin, LOW);   // LED OFF
            delay(200);
        }
    }
}
