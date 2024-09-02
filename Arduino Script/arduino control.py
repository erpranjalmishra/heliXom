import serial
import threading
import sys
import time

# Initialize serial connection to Arduino on COM5
arduino = serial.Serial('COM5', 9600, timeout=1)  # Update 'COM5' to match your port

# Function to handle user input in a separate thread
def handle_input():
    while True:
        command = input()
        if command.lower() == 'sos':
            arduino.write(b'sos\n')  # Send "sos" to Arduino to start blinking the LED
        elif command.lower() == 'stop':
            arduino.write(b'stop\n')  # Send "stop" to Arduino to stop blinking the LED

# Start the input thread
input_thread = threading.Thread(target=handle_input)
input_thread.daemon = True  # This ensures the thread will exit when the main program exits
input_thread.start()

# Main loop to read data from Arduino
try:
    while True:
        data = arduino.readline().decode('utf-8').strip()
        if data:
            print(data)

        time.sleep(0.1)  # Small delay to prevent excessive CPU usage

except KeyboardInterrupt:
    print("Exiting...")
    arduino.close()
    sys.exit(0)
