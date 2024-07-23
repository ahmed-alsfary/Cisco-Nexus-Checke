# show_err_disabled.py

from netmiko import ConnectHandler
from devices import devices

def show_err_disabled(device):
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

        # Execute the command to show interfaces with err-disabled status
        output = net_connect.send_command('show interface status err-disabled')

        # Extract relevant information
        lines = output.splitlines()
        err_disabled_interfaces = []
        for line in lines:
            if 'err-disabled' in line:
                err_disabled_interfaces.append(line.strip())
        
        # Display results
        if err_disabled_interfaces:
            print(f"Err-Disabled Interfaces for device {device['host']}:\n")
            for interface in err_disabled_interfaces:
                print(interface)
            print("\n")
        else:
            print(f"No Err-Disabled Interfaces found for device {device['host']}\n")

        # Disconnect from the device
        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to connect to device {device['host']}. Error: {e}")

# Function to run err-disabled check on all devices
def run_show_err_disabled():
    for device in devices:
        show_err_disabled(device)
