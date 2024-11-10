# About Us

Welcome to the **Admin Panel for Blue Ocean**. This app allows you to manage and view user credentials securely. It is built using **Streamlit** for the front-end interface and **MongoDB Atlas** to store the usernames and passwords.

## Features:
- **Admin Login**: The admin can log in using the credentials:  
  - **Username**: #### 
  - **Password**: ####
  This ensures that only authorized users can view sensitive data.

- **View Credentials**: After logging in as the admin, the app fetches and displays a list of all stored usernames and passwords from the MongoDB database. The data is displayed in a table-like format, making it easy to view all the credentials.

- **MongoDB Integration**: User credentials are securely saved in a **MongoDB Atlas** database. This allows easy retrieval and management of user data.

- **Streamlit Interface**: The app uses **Streamlit** to create a simple, interactive interface for both the admin login and the data display.

## Login URL:
To access the admin panel, use the following link:  
**Admin Login**: [https://weblog.streamlit.app/](https://weblog.streamlit.app/)

## Summary of the Code:
1. **Admin Login**: A simple form is provided to input the admin username and password. Only the correct credentials (`Vishal` / `Vishal123`) will grant access.
2. **MongoDB**: The app connects to a **MongoDB Atlas** database using the connection string and retrieves user credentials stored in the `credentials` collection.
3. **Data Display**: Upon successful admin login, the app fetches user data and displays it in a table using **pandas**, providing an Excel-like view.

## Future Enhancements:
- **Password Hashing**: To enhance security, passwords should be hashed before storing them in the database.
- **User Management**: Expand the functionality to allow admins to delete or update credentials.
- **Audit Log**: Implement an audit log to track who accessed the admin panel.

## URL:
- User Login: [https://blueinsta.streamlit.app/](https://blueinsta.streamlit.app/)
