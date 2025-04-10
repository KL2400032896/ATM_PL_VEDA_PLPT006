🏗️ System Components
1. Database (SQLite)
The system uses a table named users in an SQLite database file called atm.db.

🔢 Fields in the users table:
account_number: Unique 12-digit ID (Primary Key)

name: User’s full name

pin: 4-digit secret PIN for authentication

balance: Current balance in the user’s account (stored as a floating-point number)

SQLite ensures that all user data is stored securely and can be retrieved or updated in real-time.

2. Python Application
The Python script, typically named atm_app.py, handles all the logic and interaction with the database.

🧠 Key Responsibilities:
User Interface: Displays menus and takes inputs from the user via terminal/console

Input Handling: Accepts and validates account numbers, PINs, and transaction amounts

SQL Queries: Sends commands to SQLite for reading or modifying account data

Business Logic: Includes PIN verification, balance updates, and security checks

🔐 Login System
The user is prompted to enter their Account Number and 4-digit PIN.

The program connects to the SQLite database using Python’s built-in sqlite3 module.

A query checks if a user exists with the provided credentials.

If the credentials match a record in the database:

✅ Login is successful, and the user is directed to the main menu.

If they don’t match:

❌ Access is denied, and the user is prompted to try again or exit.
