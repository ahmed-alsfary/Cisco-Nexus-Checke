from show_tx_rx import run_show_tx_rx
from show_empty_rx import run_show_empty_rx
from show_err_disabled import run_show_err_disabled
from backup_config import run_backup_config

# Options menu
def main():
    print("Select an option:")
    print("1. Show interfaces with Tx and Rx Power")
    print("2. Show interfaces with Rx Power as N/A")
    print("3. Show interfaces with err-disabled status")
    print("4. Backup device configurations")
    option = input("Enter your choice (1, 2, 3, or 4): ")

    if option == "1":
        run_show_tx_rx()
    elif option == "2":
        run_show_empty_rx()
    elif option == "3":
        run_show_err_disabled()
    elif option == "4":
        run_backup_config()
    else:
        print("Invalid option. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
