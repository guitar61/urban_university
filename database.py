from crud_functions import initiate_db, populate_products

# Initialize the database and populate with sample products
initiate_db()         # This will create the Products table if it doesn't exist
populate_products()    # This will insert sample products if they don't already exist

print("Database initialized and populated with sample products.")
