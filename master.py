import serial
import time
import RPi.GPIO as GPIO

ser = serial.Serial('/dev/serial0', 9600)
time.sleep(2)

def send_command(command):
    ser.write(f"{command}\n".encode())
    print(f"[DEBUG] Sent command: {command}")

# GPIO config
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up all the GPIO pins
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
# GPIO.setup(14, GPIO.OUT)      UART RX/TX
# GPIO.setup(15, GPIO.OUT)      UART RX/TX
GPIO.setup(16, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

# Set all pins to be low
GPIO.output(2, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(4, GPIO.LOW)
GPIO.output(5, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(7, GPIO.LOW)
GPIO.output(8, GPIO.LOW)
GPIO.output(9, GPIO.LOW)
GPIO.output(10, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(12, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
# GPIO.output(14, GPIO.LOW)     UART RX/TX
# GPIO.output(15, GPIO.LOW)     UART RX/TX
GPIO.output(16, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.output(18, GPIO.LOW)
GPIO.output(19, GPIO.LOW)
GPIO.output(20, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)    
GPIO.output(26, GPIO.LOW)
GPIO.output(27, GPIO.LOW)