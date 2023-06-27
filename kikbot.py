from kik import KikApi, Configuration
from kik.messages import TextMessage
import time
import random

# Initialize the Kik API
kik = KikApi('your_bot_username', 'your_api_key')
config = Configuration(webhook='https://your-webhook-url.com')
kik.set_configuration(config)

# Define the list of possible random messages. Create a "" string to add your messages fx "Hello",.
messages = [
    "To anger a conservative, lie to him. To anger a liberal, tell him the truth!",
    "Fart?",
    "Spaghetti!",
    "Greetings from your Kik bot!",
    "Trumo 2024",
    "Sleepy joe",
    "The modern conservative is engaged in one of man's oldest exercises in moral philosophy; that is, the search for a superior moral justification for selfishness.?"
]

# Define the interval and number of random messages
interval_minutes = 60  # Change this to set the interval in seconds
num_messages = 1  # Change this to set the number of random messages to send

# Function to send random messages
def send_random_messages():
    for _ in range(num_messages):
        message = random.choice(messages)
        kik.send_messages([TextMessage(to='your_kik_username', body=message)])
        time.sleep(1)  # Add a short delay between messages

# Loop to send random messages at the specified interval
while True:
    send_random_messages()
    time.sleep(interval_minutes)
