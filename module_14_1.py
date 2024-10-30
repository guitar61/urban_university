import sqlite3

# Step 1: Connect to the database
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Step 2: Create the Users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')
connection.commit()

print("Database and Users table created.")

# Insert 10 records into the Users table
users_data = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

cursor.executemany('''
    INSERT INTO Users (username, email, age, balance) 
    VALUES (?, ?, ?, ?)
''', users_data)
connection.commit()

print("10 records inserted.")


# Update balance to 500 for every 2nd user starting with the 1st
for i in range(1, 11, 2):  # Indices 1, 3, 5, 7, 9 (1-based)
    cursor.execute('''
        UPDATE Users
        SET balance = 500
        WHERE id = ?
    ''', (i,))
connection.commit()

print("Balance updated for every 2nd record starting with the 1st.")


# Delete every 3rd user starting with the 1st
for i in range(1, 11, 3):  # Indices 1, 4, 7, 10 (1-based)
    cursor.execute('''
        DELETE FROM Users
        WHERE id = ?
    ''', (i,))
connection.commit()

print("Every 3rd record deleted starting with the 1st.")


# Fetch records where age is not 60
cursor.execute('''
    SELECT username, email, age, balance
    FROM Users
    WHERE age != 60
''')
users = cursor.fetchall()

# Display the fetched records in the specified format
print("Console output:")
for user in users:
    username, email, age, balance = user
    print(f"Name: {username} | Email: {email} | Age: {age} | Balance: {balance}")
