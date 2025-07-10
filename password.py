import serial
import time

# Update with the correct serial port (e.g., COM3 if you changed it)
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Wait for the serial connection to initialize

def send_password(password):
    ser.write(password.encode() + b'\n')
    print(f"Sent: {password}")

try:
    while True:
        password = input("Enter password to unlock the solenoid: ")
        send_password(password)
        print("Password sent to Arduino. Waiting for response...")
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated.")
finally:
    ser.close()
