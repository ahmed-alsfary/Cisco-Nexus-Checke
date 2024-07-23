# backup_config.py

from netmiko import ConnectHandler
from devices import devices
import os
from datetime import datetime

def backup_config(device):
    try:
        # Connection settings for Nexus device
        device_params = {
            'device_type': 'cisco_nxos',
            'host': device['host'],
            'username': device['username'],
            'password': device['password'],
            'secret': device['secret'],
        }

        # Connect to the device
        net_connect = ConnectHandler(**device_params)
        net_connect.enable()

        # Execute the command to show the running configuration
        output = net_connect.send_command('show running-config')

        # Create backup directory if it does not exist
        backup_dir = 'backups'
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Generate the backup file name
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_file = f"{backup_dir}/{device['host']}_backup_{timestamp}.txt"

        # Save the running configuration to the backup file
        with open(backup_file, 'w') as f:
            f.write(output)

        print(f"Backup of device {device['host']} completed successfully. Saved to {backup_file}")

        # Disconnect from the device
        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to backup device {device['host']}. Error: {e}")

# Function to run backup on all devices
def run_backup_config():
    for device in devices:
        backup_config(device)
