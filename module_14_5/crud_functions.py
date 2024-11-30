import sqlite3


# Function to initialize the database and create the Products table
def initiate_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                      id INTEGER PRIMARY KEY,
                      title TEXT NOT NULL,
                      description TEXT,
                      price INTEGER NOT NULL)''')

    # Create Users table (if not exist)
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT NOT NULL UNIQUE,
                      email TEXT NOT NULL,
                      age INTEGER NOT NULL,
                      balance INTEGER NOT NULL DEFAULT 1000)''')
    conn.commit()
    conn.close()

    # Function to add a new user to the Users table


def add_user(username, email, age):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)", (username, email, age))
    conn.commit()
    conn.close()


def is_included(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user is not None


# Function to get all products from the Products table
def get_all_products():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, price FROM Products")
    products = cursor.fetchall()
    conn.close()
    return products


# Optional: Function to populate the Products table with sample data
def populate_products():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Sample products
    products = [
        (1, "Product 1", "Description for product 1", 100),
        (2, "Product 2", "Description for product 2", 200),
        (3, "Product 3", "Description for product 3", 300),
        (4, "Product 4", "Description for product 4", 400)
    ]

    # Insert products, ignore if they already exist (avoiding UNIQUE constraint errors)
    cursor.executemany("INSERT OR IGNORE INTO Products VALUES (?, ?, ?, ?)", products)
    conn.commit()
    conn.close()
