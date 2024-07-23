# main.py

import warnings
from cryptography.utils import CryptographyDeprecationWarning
from show_tx_rx import run_show_tx_rx
from show_empty_rx import run_show_empty_rx
from show_err_disabled import run_show_err_disabled

# Suppress CryptographyDeprecationWarning
warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

# Options menu
def main():
    print("Select an option:")
    print("1. Show interfaces with Tx and Rx Power")
    print("2. Show interfaces with Rx Power as N/A")
    print("3. Show interfaces with err-disabled status")
    option = input("Enter your choice (1, 2, or 3): ")

    if option == "1":
        run_show_tx_rx()
    elif option == "2":
        run_show_empty_rx()
    elif option == "3":
        run_show_err_disabled()
    else:
        print("Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
