import getpass

def load_data():
    try:
        with open("data.txt", "r") as f:
            lines = f.readlines()
            data = {}
            for line in lines:
                pin, name, balance = line.strip().split(",")
                data[pin] = {
                    "name": name,
                    "balance": float(balance)
                }
            return data
    except FileNotFoundError:
        return {
            "1234": {"name": "Vaishnavi", "balance": 1000.0}
        }

def save_data(data):
    with open("data.txt", "w") as f:
        for pin, info in data.items():
            f.write(f"{pin},{info['name']},{info['balance']}\n")

def authenticate_user(pin, data):
    return pin in data

def show_menu():
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

def check_balance(pin, data):
    print(f"{data[pin]['name']}, your current balance is: ₹{data[pin]['balance']:.2f}\n")

def withdraw_money(pin, data):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Invalid amount.\n")
        elif amount > data[pin]['balance']:
            print("Insufficient balance.\n")
        else:
            data[pin]['balance'] -= amount
            print(f"₹{amount:.2f} withdrawn successfully.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def deposit_money(pin, data):
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("Invalid amount.\n")
        else:
            data[pin]['balance'] += amount
            print(f"₹{amount:.2f} deposited successfully.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def get_pin_input():
    try:
        return getpass.getpass("Enter your 4-digit PIN (input hidden): ")
    except Exception as e:
        print("Error:", e)
        return input("Enter PIN (fallback): ")
