# show_tx_rx.py

from netmiko import ConnectHandler
from devices import devices

def show_tx_rx(device):
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

        # Execute the command to show transceiver details
        output = net_connect.send_command('show interface transceiver details')

        # Extract relevant information
        lines = output.splitlines()
        current_port = None
        fiber_interfaces = []
        for line in lines:
            if line.startswith('Ethernet'):
                current_port = line.strip()
                tx_power, rx_power = None, None
            if 'transceiver is present' in line:
                transceiver_present = True
            if 'type is' in line:
                transceiver_type = line.split('type is')[1].strip()
            if 'Tx Power' in line:
                tx_power = line.split()[2]
            if 'Rx Power' in line:
                rx_power = line.split()[2]
                if tx_power != 'N/A' or rx_power != 'N/A':
                    fiber_interfaces.append((current_port, tx_power, rx_power))
        
        # Display results
        if fiber_interfaces:
            print(f"Fiber Optic Interfaces for device {device['host']}:\n")
            for interface in fiber_interfaces:
                port, tx_power, rx_power = interface
                print(f"Port: {port}, Tx Power: {tx_power}, Rx Power: {rx_power}")
            print("\n")
        else:
            print(f"No Fiber Optic Interfaces with Tx and Rx Power found for device {device['host']}\n")

        # Disconnect from the device
        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to connect to device {device['host']}. Error: {e}")

# Function to run Tx and Rx power check on all devices
def run_show_tx_rx():
    for device in devices:
        show_tx_rx(device)