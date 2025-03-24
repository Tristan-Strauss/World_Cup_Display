import serial

ser = serial.Serial('/dev/serial0', 9600)

while True:
    if ser.is_waiting > 0:
        command = ser.readline().decode().strip()
        print(f"[DEBUG] Received command: {command}")
        