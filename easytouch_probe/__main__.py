#!/usr/bin/env python3

import RPi.GPIO as GPIO
import serial
import time
import binascii

# Constants
SERIAL_PORT = '/dev/ttyAMA2'
BAUD_RATE = 9600
GPIO_DE_RE = 6  # GPIO6 for RS485_1 DE/RE control

# Example probe frame (based on nodejs-poolController and protocol traces)
# This is a simple 'heartbeat' frame used in Pentair protocol
POLL_FRAME = bytes.fromhex('FF 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00')

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Suppress 'already in use' warning
GPIO.setup(GPIO_DE_RE, GPIO.OUT)
GPIO.output(GPIO_DE_RE, GPIO.LOW)  # Default to receive mode

# Setup serial
ser = serial.Serial(
    port=SERIAL_PORT,
    baudrate=BAUD_RATE,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1
)

print(f"Polling on {SERIAL_PORT} at {BAUD_RATE} baud...")

try:
    while True:
        # 1️⃣ Enable transmit mode
        GPIO.output(GPIO_DE_RE, GPIO.HIGH)
        time.sleep(0.01)  # Brief delay to ensure driver settles

        # 2️⃣ Send poll frame
        ser.write(POLL_FRAME)
        ser.flush()
        print(f"[{time.strftime('%H:%M:%S')}] TX: {binascii.hexlify(POLL_FRAME).decode('ascii').upper()}")

        # 3️⃣ Back to receive mode
        time.sleep(0.01)
        GPIO.output(GPIO_DE_RE, GPIO.LOW)

        # 4️⃣ Wait for any response
        response = ser.read(64)  # Read up to 64 bytes (adjust if needed)
        if response:
            hex_output = binascii.hexlify(response).decode('ascii').upper()
            print(f"[{time.strftime('%H:%M:%S')}] RX: {hex_output}")

        # 5️⃣ Delay before next poll
        time.sleep(2)

except KeyboardInterrupt:
    print("\nExiting...")
finally:
    ser.close()
    GPIO.cleanup()