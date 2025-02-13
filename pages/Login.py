import streamlit as st
from pages.security_login import *

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
                    st.success("Logged in successfully!")
                    st.session_state["logged_in"] = True
                    if st.session_state.get("redirect_to_login", False):
                        st.session_state["redirect_to_login"] = False
                        st.rerun()
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
            fname = st.text_input("FirstName", label_visibility="collapsed")
        with col3:
            st.subheader("Last Name")
            lname = st.text_input("LastName", label_visibility="collapsed")
        
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.subheader("Create username")
        with col3:
            username1 = st.text_input("Username", label_visibility="collapsed")
        
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.subheader("Enter Email")
        with col3:
            email1 = st.text_input("Email", label_visibility="collapsed")
        
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.subheader("Create Password")
        with col3:
            password1 = st.text_input("Password1", type="password", label_visibility="collapsed")
        
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.subheader("Confirm Password")
        with col3:
            password2 = st.text_input("Password2", type="password", label_visibility="collapsed")
        
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
    st.title("Security")

    choice = st.radio("Choose an option:", ["Login", "Register"], index=0)

    # Show the appropriate interface based on the selected option
    if choice == "Login":
        login_interface()
    elif choice == "Register":
        register_interface()

# Run the login page when the script is executed
if __name__ == "__main__":
    login_page()
