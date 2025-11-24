#!/usr/bin/env python3
# Einfaches Teleop-Beispiel: sendet Befehle über seriellen Port an Arduino
import time
import serial
import sys

PORT = '/dev/ttyUSB0'  # anpassen (Windows z.B. COM3)
BAUD = 115200

def send(cmd):
    with serial.Serial(PORT, BAUD, timeout=1) as s:
        s.write((cmd + '\n').encode())
        time.sleep(0.1)
        resp = s.read_all().decode(errors='ignore')
        print("Antwort:", resp.strip())

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: teleop_stub.py 'MOVE JOINT1 90'")
    else:
        send(sys.argv[1])