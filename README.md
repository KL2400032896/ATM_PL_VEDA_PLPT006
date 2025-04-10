import sqlite3

# Connect to (or create) the database file
conn = sqlite3.connect('atm.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    account_number TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    pin TEXT NOT NULL,
    balance REAL DEFAULT 0.0
)
''')

# Add dummy users
dummy_users = [
    ('100011112222', 'Anjali Mehta', '1234', 5200.00),
    ('100033334444', 'Vikram Joshi', '2345', 7200.50),
    ('100055556666', 'Neha Singh', '3456', 1200.75),
    ('100077778888', 'Rajesh Patel', '4567', 8600.00),
    ('100099990000', 'Pooja Rani', '5678', 10000.00),
    ('100012341234', 'Aarav Sharma', '6789', 4300.60),
    ('100043216789', 'Meera Das', '7890', 2900.25),
    ('100078901234', 'Yash Malhotra', '8901', 150.00),
    ('100076543210', 'Kiran Rao', '9012', 400.00),
    ('100065432109', 'Tanvi Iyer', '0123', 9999.99)
]

cursor.executemany("INSERT OR IGNORE INTO users VALUES (?, ?, ?, ?)", dummy_users)

conn.commit()
conn.close()

print("✅ Database created with 10 Indian users.")


