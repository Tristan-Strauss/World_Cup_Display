import serial
import time

ser = serial.Serial("/dev/serial0", 9600)
time.sleep(2)

print("[+] Serial Connection to Slave Established")

def send_command(command):
    ser.write(f"{command}\n".encode())
    print(f"[-] Command sent to slave: {command}")

if __name__ == "__main__":
    while True:
        send_command("Test 1")
        time.sleep(2)
        send_command("Test 2")
        break