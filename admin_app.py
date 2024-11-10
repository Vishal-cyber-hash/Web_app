import streamlit as st
from pymongo import MongoClient
import pandas as pd

# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://Vishu:vdONpmr0BXz6leVg@cluster0.8q6fo.mongodb.net/yourDatabaseName?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client.get_database()  # Use your database name
credentials_collection = db.credentials  # Name of the collection

# Admin credentials
ADMIN_USERNAME = "Vishal"
ADMIN_PASSWORD = "Vishal123"

# Streamlit app
st.set_page_config(page_title="Admin Panel - Blue Ocean", page_icon="🔒")

# Admin Login
def admin_login(username, password):
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

# Function to display all credentials
def display_credentials():
    # Retrieve all documents from MongoDB
    credentials_data = credentials_collection.find()
    # Convert the MongoDB cursor to a list of dictionaries
    credentials_list = list(credentials_data)
    # Convert to a DataFrame for Excel-like display
    df = pd.DataFrame(credentials_list)
    if not df.empty:
        # Drop the MongoDB object id column (it will be a column named '_id')
        df = df.drop(columns=["_id"])
    st.write(df)

# Admin Login Page
st.title("Admin Panel - Blue Ocean")

admin_username = st.text_input("Admin Username", "")
admin_password = st.text_input("Admin Password", type="password")

if st.button("Admin Login"):
    if admin_login(admin_username, admin_password):
        st.success("Admin login successful!")
        # Now show the user credentials in an Excel-like table
        display_credentials()
    else:
        st.error("Invalid admin credentials. Please try again.")
