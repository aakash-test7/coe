import streamlit as st
from pages.security_login import *

# Initialize session state variables if they are not present
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'current_interface' not in st.session_state:
    st.session_state.current_interface = "Login"  # Default to "Login"

# Function to clear registration inputs
def clear_register_inputs():
    st.session_state.register_username1 = ""
    st.session_state.register_password1 = ""
    st.session_state.register_password2 = ""
    st.session_state.register_fname = ""
    st.session_state.register_lname = ""
    st.session_state.register_email1 = ""

# Function to clear login inputs
def clear_login_inputs():
    st.session_state.login_username = ""
    st.session_state.login_password = ""

# Login interface
def login_interface():
    with st.container(border=True):
        col1, col2, col3, col4, col5 = st.columns(5)
        with col3:
            st.title("Login")
        
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.subheader("Enter Username")
        with col3:
            username = st.text_input("Username", key="login_username", label_visibility="collapsed")
        
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.subheader("Enter Password")
        with col3:
            password = st.text_input("Password", key="login_password", type="password", label_visibility="collapsed")
        
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 2, 1, 1, 1])
        with col4:
            if st.button("Continue", use_container_width=True):
                st.success("Checking credentials")
                if check_user(username, password):
                    st.session_state['authenticated'] = True
                    st.success("Logged in successfully!")
                    st.title(f"Welcome user")
                    conn = connect_to_db()
                    cursor = conn.cursor()
                    # Fetch user details
                    query5 = "SELECT FirstName FROM Identity WHERE Username = %s"
                    cursor.execute(query5, (username,))
                    user_info = cursor.fetchone()
                    if user_info:
                        st.title(f"Hello {user_info[0]}!")
                    else:
                        st.title("User information not found.")
                    query6 = "SELECT LastName FROM Identity WHERE Username = %s"
                    cursor.execute(query6, (username,))
                    user_info = cursor.fetchone()
                    if user_info:
                        st.title(f"Hello {user_info[0]}!")
                    else:
                        st.title("User information not found.")
                    query7 = "SELECT Email FROM Identity WHERE Username = %s"
                    cursor.execute(query7, (username,))
                    user_info = cursor.fetchone()
                    if user_info:
                        st.title(f"Hello {user_info[0]}!")
                    else:
                        st.title("User information not found.")
                    st.session_state.authenticated = True

                else:
                    st.error("Invalid username or password")

# Registration interface
def register_interface():
    with st.container(border=True):
        col1, col2, col3, col4, col5 = st.columns(5)
        with col3:
            st.title("Register")
        
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.subheader("First Name")
            fname = st.text_input("FirstName", key="register_fname", label_visibility="collapsed")
        with col3:
            st.subheader("Last Name")
            lname = st.text_input("LastName", key="register_lname", label_visibility="collapsed")
        
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.subheader("Create username")
        with col3:
            username1 = st.text_input("Username", key="register_username1", label_visibility="collapsed")
        
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.subheader("Enter Email")
        with col3:
            email1 = st.text_input("Email", key="register_email1", label_visibility="collapsed")
        
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.subheader("Create Password")
        with col3:
            password1 = st.text_input("Password1", type="password", key="register_password1", label_visibility="collapsed")
        
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.subheader("Confirm Password")
        with col3:
            password2 = st.text_input("Password2", type="password", key="register_password2", label_visibility="collapsed")
        
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 2, 1, 1, 1])
        with col4:
            if st.button("Register", use_container_width=True):
                if password1 == password2:
                    st.success("Password checked")
                    if not validate_username(username1):
                        st.error("Invalid username. Only a-z, A-Z, 0-9, and !@#$%^&*_+-/? are allowed.")
                    elif not validate_email(email1):
                        st.error("Invalid email. Must contain @ and .com.")
                    elif not validate_password(password1):
                        st.error("Password must be at least 8 characters long.")
                    else:
                        if add_user(username1, password1, fname, lname, email1):
                            st.success("Registration successful! Please login.")
                        else:
                            st.error("Username or email already exists.")
                else:
                    st.warning("Passwords do not match. Please try again.")

# Main function for login page logic
def login_page():
    # Ensure session state is initialized
    if 'current_interface' not in st.session_state:
        st.session_state.current_interface = "Login"
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    st.title("Security")

    choice = st.radio("Choose an option:", ["Login", "Register"], index=0 if st.session_state.current_interface == "Login" else 1)

    # If user switches the interface, confirm action and reload
    if st.session_state.current_interface != choice:
        st.warning("Are you sure you want to switch? Unsaved changes will be lost.")
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col3:
            if st.button("Yes"):
                st.session_state.current_interface = choice
                st.rerun()
        with col5:
            if st.button("No"):
                st.rerun()

    # Update current interface session state
    st.session_state.current_interface = choice

    # Show the appropriate interface based on the selected option
    if st.session_state.current_interface == "Login":
        login_interface()
    elif st.session_state.current_interface == "Register":
        register_interface()

# Run the login page when the script is executed
if __name__ == "__main__":
    login_page()
