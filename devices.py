# devices.py

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

username = os.getenv('DEVICE_USERNAME')
password = os.getenv('PASSWORD')
enable_password = os.getenv('ENABLE_PASSWORD')

# Print the values to verify
print(f"Username: {username}")
print(f"Password: {password}")
print(f"Enable Password: {enable_password}")

devices = [
    {
        'host': '192.168.51.57',
        'username': username,
        'password': password,
        'secret': enable_password,  # Update with enable password if applicable
    },
    {
        'host': '192.168.51.49',
        'username': username,
        'password': password,
        'secret': enable_password,  # Update with enable password if applicable
    },
    {
        'host': '192.168.51.60',
        'username': username,
        'password': password,
        'secret': enable_password,  # Update with enable password if applicable
    },
    # Add more devices here if needed
]
