from kik import KikApi, Configuration
from kik.messages import TextMessage
import time
import random

# Initialize the Kik API
kik = KikApi('your_bot_username', 'your_api_key')
config = Configuration(webhook='https://your-webhook-url.com')
kik.set_configuration(config)

# Define the list of possible random messages. Add your own messages here.
messages = [
    "To anger a conservative, lie to him. To anger a liberal, tell him the truth!",
    "Fart?",
    "Spaghetti!",
    "Greetings from your Kik bot!",
    "Trump 2024",
    "Sleepy Joe",
    "The modern conservative is engaged in one of man's oldest exercises in moral philosophy; that is, the search for a superior moral justification for selfishness.",
]

# Define the interval and number of random messages
interval_minutes = 60  # Change this to set the interval in minutes
num_messages = 1  # Change this to set the number of random messages to send

# Function to send random messages
def send_random_messages():
    for _ in range(num_messages):
        message = random.choice(messages)
        kik.send_messages([TextMessage(to='your_kik_username', body=message)])
        time.sleep(1)  # Add a short delay between messages

# Event handler for incoming text messages
@kik.on_text
def handle_text_message(message):
    # Process the incoming text message
    # Send a response or perform necessary actions
    pass

# Event handler for incoming scan data
@kik.on_scan_data
def handle_scan_data(message):
    # Process the incoming scan data
    # Send a response or perform necessary actions
    pass

# Loop to send random messages at the specified interval
while True:
    send_random_messages()
    time.sleep(interval_minutes * 60)  # Convert minutes to seconds

