import sqlite3

# Connect to the database (creates atm.db if not exists)
conn = sqlite3.connect('atm.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    account_number TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    pin TEXT NOT NULL,
    balance REAL DEFAULT 0.0
)
''')
conn.commit()

# Function to verify PIN again before operations
def verify_pin(user):
    pin_attempt = input("🔐 Re-enter your PIN to continue: ")
    return pin_attempt == user[2]

# Function to check balance
def check_balance(user):
    if verify_pin(user):
        print(f"✅ Your current balance is: ₹{user[3]:.2f}")
    else:
        print("❌ Incorrect PIN! Operation cancelled.")

# Function to deposit money
def deposit(user):
    if verify_pin(user):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print("❌ Invalid amount.")
                return
            new_balance = user[3] + amount
            cursor.execute("UPDATE users SET balance=? WHERE account_number=?", (new_balance, user[0]))
            conn.commit()
            print(f"✅ ₹{amount:.2f} deposited. New Balance: ₹{new_balance:.2f}")
            user = get_user(user[0])  # Refresh user balance
        except ValueError:
            print("❌ Please enter a valid number.")
    else:
        print("❌ Incorrect PIN! Deposit cancelled.")

# Function to withdraw money
def withdraw(user):
    if verify_pin(user):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("❌ Invalid amount.")
                return
            if amount > user[3]:
                print("❌ Insufficient funds!")
                return
            new_balance = user[3] - amount
            cursor.execute("UPDATE users SET balance=? WHERE account_number=?", (new_balance, user[0]))
            conn.commit()
            print(f"✅ ₹{amount:.2f} withdrawn. New Balance: ₹{new_balance:.2f}")
            user = get_user(user[0])  # Refresh user balance
        except ValueError:
            print("❌ Please enter a valid number.")
    else:
        print("❌ Incorrect PIN! Withdrawal cancelled.")

# Function to fetch user from DB
def get_user(account_number):
    cursor.execute("SELECT * FROM users WHERE account_number=?", (account_number,))
    return cursor.fetchone()

# Main loop
def main():
    print("🏦 Welcome to the Python ATM!")

    account_number = input("Enter your Account Number: ")
    pin = input("Enter your 4-digit PIN: ")

    user = get_user(account_number)

    if user and user[2] == pin:
        print(f"\n👋 Welcome, {user[1]}!")
        while True:
            print("\n--- Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                check_balance(user)
                user = get_user(account_number)  # Refresh balance
            elif choice == '2':
                deposit(user)
                user = get_user(account_number)
            elif choice == '3':
                withdraw(user)
                user = get_user(account_number)
            elif choice == '4':
                print("👋 Thank you for using the ATM. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Try again.")
    else:
        print("❌ Invalid account number or PIN.")

    conn.close()

# Run program
if __name__ == "__main__":
    main()
