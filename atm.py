try:
    from bank import (
        load_data, save_data, authenticate_user,
        show_menu, check_balance, withdraw_money,
        deposit_money, get_pin_input
    )
except ImportError:
    from bank import (
        load_data, save_data, authenticate_user,
        show_menu, check_balance, withdraw_money,
        deposit_money
    )
    def get_pin_input():
        return input("Enter your 4-digit PIN: ")

def main():
    user_data = load_data()

    print("==== Welcome to Python ATM ====")
    pin = get_pin_input()

    if authenticate_user(pin, user_data):
        print(f"Login successful! Welcome, {user_data[pin]['name']}.\n")
        while True:
            show_menu()
            choice = input("Select option (1-4): ")

            if choice == '1':
                check_balance(pin, user_data)
            elif choice == '2':
                withdraw_money(pin, user_data)
            elif choice == '3':
                deposit_money(pin, user_data)
            elif choice == '4':
                save_data(user_data)
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Try again.\n")
    else:
        print("Invalid PIN. Access denied.")

if __name__ == "__main__":
    main()
