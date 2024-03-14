from pymongo import MongoClient
from decouple import config

# MongoDB connection string (replace with your actual credentials)
conn_str = config('DB_LINK')
client = MongoClient(conn_str)

def get_client():
    """Returns the MongoDB client instance."""
    return client

# Test the connection (optional)
try:
    client.server_info()
    print("Connected to MongoDB successfully!")
except Exception as e:
    print("Error connecting to MongoDB:", e)


db = client['erp']
products_collection = db['products']
cart_collection = db['cart']
sales_collection = db['sales']