
### `README.md`

```markdown
# Cisco Interface Checker

## Overview

The Cisco Interface Checker project provides a set of Python scripts to check various statuses of interfaces on Cisco Nexus devices. It includes functionalities to:
- Show interfaces with Tx and Rx power
- Find interfaces with Rx power as "N/A"
- Identify interfaces with an err-disabled status

## File Structure

- `devices.py`: Contains the connection settings for the devices.
- `show_tx_rx.py`: Contains the function to show interfaces with Tx and Rx power.
- `show_empty_rx.py`: Contains the function to show interfaces with Rx power as "N/A".
- `show_err_disabled.py`: Contains the function to show interfaces with err-disabled status.
- `main.py`: Contains the main options menu to run the different functions.

## Prerequisites

- Python 3.x
- `netmiko` library

You can install the `netmiko` library using pip:

```sh
pip install netmiko
```

## Setup

1. **Clone the repository**:

    ```sh
    git clone https://github.com/ahmed-alsfary/Cisco-Nexus-Checke.git
    cd Cisco-Nexus-Checke
    ```

2. **Edit `devices.py`** to include the connection settings for your Cisco Nexus devices:

    ```python
    devices = [
        {
            'host': '192.168.51.57',
            'username': 'username',
            'password': 'password',
            'secret': 'YOUR_ENABLE_PASSWORD',  # Update with enable password if applicable
        },
        {
            'host': '192.168.51.49',
            'username': 'username',
            'password': 'password',
            'secret': 'YOUR_ENABLE_PASSWORD',  # Update with enable password if applicable
        },
        {
            'host': '192.168.51.60',
            'username': 'username',
            'password': 'password',
            'secret': 'YOUR_ENABLE_PASSWORD',  # Update with enable password if applicable
        },
        # Add more devices here if needed
    ]
    ```

## Usage

1. **Run the main script**:

    ```sh
    python main.py
    ```

2. **Select an option**:

    - Enter `1` to show interfaces with Tx and Rx power
    - Enter `2` to show interfaces with Rx power as "N/A"
    - Enter `3` to show interfaces with err-disabled status

## Scripts Description

### `devices.py`

Contains the connection settings for the Cisco Nexus devices.

### `show_tx_rx.py`

Contains the function to show interfaces with Tx and Rx power. It connects to each device, runs the command `show interface transceiver details`, and extracts the relevant information.

### `show_empty_rx.py`

Contains the function to show interfaces with Rx power as "N/A". It connects to each device, runs the command `show interface transceiver details`, and finds interfaces where the Rx power is "N/A".

### `show_err_disabled.py`

Contains the function to show interfaces with err-disabled status. It connects to each device, runs the command `show interface status err-disabled`, and extracts the relevant information.

### `main.py`

Provides the main options menu to run the different functions. It allows the user to select between showing interfaces with Tx and Rx power, showing interfaces with Rx power as "N/A", and showing interfaces with err-disabled status.

## Example Output

After running `main.py` and selecting an option, the script will connect to each device and display the relevant information.

### Option 1: Show interfaces with Tx and Rx Power

```
Fiber Optic Interfaces for device 192.168.51.57:

Port: Ethernet1/1, Tx Power: -1.2 dBm, Rx Power: -3.4 dBm
Port: Ethernet1/2, Tx Power: -1.1 dBm, Rx Power: -3.3 dBm

No Fiber Optic Interfaces with Tx and Rx Power found for device 192.168.51.49

...
```

### Option 2: Show interfaces with Rx Power as N/A

```
Interfaces with Rx Power as N/A for device 192.168.51.57:

Port: Ethernet1/3, Tx Power: -1.2 dBm, Rx Power: N/A
Port: Ethernet1/4, Tx Power: -1.1 dBm, Rx Power: N/A

No Interfaces with Rx Power as N/A found for device 192.168.51.49

...
```

### Option 3: Show interfaces with err-disabled status

```
Err-Disabled Interfaces for device 192.168.51.57:

Ethernet1/1 is err-disabled
Ethernet1/2 is err-disabled

No Err-Disabled Interfaces found for device 192.168.51.49

...
```

## Troubleshooting

If you encounter any issues while running the scripts, please ensure that:

- The `netmiko` library is installed.
- The device connection settings in `devices.py` are correct.
- Your network allows SSH connections to the specified devices.

Feel free to raise an issue if you encounter any problems.

## License

This project is licensed under the MIT License.
```

### How to Use the README

1. **Save the `README.md` file** in the root directory of your project.
2. **Push the changes to your GitHub repository**.

```sh
git add README.md
git commit -m "Add README file"
git push origin main
```

If you have any further questions or need additional adjustments, feel free to ask.
