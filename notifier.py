import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK")

def send_message(content):
    if not WEBHOOK_URL:
        print("❌ Webhook URL not found in .env.")
        return

    data = {"content": content}
    try:
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print("✅ Message sent to Discord successfully.")
        else:
            print(f"❌ Failed to send: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Error sending message: {e}")
