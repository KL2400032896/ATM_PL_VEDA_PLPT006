import json
import os

# Constants
DATA_FILE = 'atm_data.json'

# User class to represent an ATM user
class User:
    def __init__(self, pin, balance=0.0):
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

# Function to load user data from a file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save user data to a file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file)

# Function to authenticate user by PIN
def authenticate_user(pin, users):
    return users.get(pin)

# ATM menu function
def atm_menu(user):
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            print(f"Your current balance is: ${user.check_balance():.2f}")
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                if user.deposit(amount):
                    print(f"${amount:.2f} deposited successfully.")
                else:
                    print("Invalid deposit amount.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                if user.withdraw(amount):
                    print(f"${amount:.2f} withdrawn successfully.")
                else:
                    print("Invalid withdrawal amount or insufficient funds.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the ATM. Thank you!")
            break
        else:
            print("Invalid option. Please try again.")

# Main function to run the ATM simulation
def main():
    users_data = load_data()
    users = {pin: User(pin, data['balance']) for pin, data in users_data.items()}

    pin = input("Enter your PIN: ")
    user = authenticate_user(pin, users)

    if user is None:
        print("User  not found. Creating a new account.")
        user = User(pin)
        users[pin] = user
        save_data({pin: {'balance': user.balance}})

    # Display the ATM menu after authentication
    atm_menu(user)
    # Save the user's balance after operations
    save_data({pin: {'balance': user.balance}})

if __name__ == "__main__":
    main()