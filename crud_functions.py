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
    conn.commit()
    conn.close()


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
