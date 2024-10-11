# -*- coding: utf-8 -*-
import subprocess

def upload_arduino_code():
    # �Ƶ��̳� ����ġ ������ ���� ��θ� �����ϼ���
    arduino_sketch_path = "/home/casptone/Downloads/yolov5-master/arduino_invscode/arduino_led_control.ino"
    
    compile_command = [
        "arduino-cli", "compile", "--fqbn", "arduino:avr:uno", arduino_sketch_path
    ]
    upload_command = [
        "arduino-cli", "upload", "-p", "/dev/ttyUSB0", "--fqbn", "arduino:avr:uno", arduino_sketch_path
    ]

    # ����ġ ������
    subprocess.run(compile_command, check=True)
    # ������ �� �Ƶ��̳� ���忡 ���ε�
    subprocess.run(upload_command, check=True)

if __name__ == "__main__":
    try:
        upload_arduino_code()
        print("Arduino code uploaded successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
