#!/usr/bin/env python3

import RPi.GPIO as GPIO
import serial
import time
import binascii

# Constants
SERIAL_PORT = '/dev/ttyAMA2'
BAUD_RATE = 9600
GPIO_DE_RE = 6  # GPIO6 for RS485_1 DE/RE control

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_DE_RE, GPIO.OUT)
GPIO.output(GPIO_DE_RE, GPIO.LOW)  # Default to receive mode

# Setup serial
ser = serial.Serial(
    port=SERIAL_PORT,
    baudrate=BAUD_RATE,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1  # 1 second timeout for read
)

print(f"Listening on {SERIAL_PORT} at {BAUD_RATE} baud...")
try:
    while True:
        if ser.in_waiting > 0:
            data = ser.read(ser.in_waiting)
            hex_output = binascii.hexlify(data).decode('ascii').upper()
            print(f"[{time.strftime('%H:%M:%S')}] RX: {hex_output}")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    ser.close()
    GPIO.cleanup()