import sqlite3

# Connect to the existing database
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Step 1: Delete the user with id=6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
connection.commit()

# Step 2: Count the total number of users
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Step 3: Calculate the sum of all balances
cursor.execute("SELECT SUM(balance) FROM Users")
all_balance = cursor.fetchone()[0]

# Step 4: Calculate the average balance
average_balance = all_balance / total_users

# Output the result
print(f"Average balance of all users: {average_balance:.1f}")

# Close the database connection
connection.close()