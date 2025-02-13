import streamlit as st
from backend import user_input_menu, multi_user_input_menu, process_locid, process_mlocid
from pages.footer_all import base_footer 

def search_page():
    st.title("Search")
    st.write("**Begin the search by interacting with the backend process.**")
    col1, col2 = st.columns(2)

    with col1:
        con1=st.container(border=True)
        tid = con1.text_input("Enter the Gene ID: ", placeholder="e.g., Ca_00001", key="Tid_input1").strip()
        mtid = con1.text_input("Enter multiple Gene IDs: ", placeholder="e.g., Ca_00001, Ca_00002", key="mTid_input2").strip()
        if mtid:
            mtid_list = [item.strip() for item in mtid.replace(",", " ").split()]
            mtid_list = list(set(mtid_list))
            mtid = ",".join(mtid_list)

    with col2:
        con2=st.container(border=True)
        locid = con2.text_input("Enter the NCBI ID: ", placeholder="e.g., LOC101511858", key="Locid_input1").strip()
        mlocid = con2.text_input("Enter multiple NCBI IDs: ", placeholder="e.g., LOC101511858, LOC101496413", key="mLocid_input2").strip()
        if mlocid:
            mlocid_list = [item.strip() for item in mlocid.replace(",", " ").split()]
            mlocid_list = list(set(mlocid_list))
            mlocid = ",".join(mlocid_list)
    con1,con2,con3=st.columns([2,2,2])
    with con2:
        start_button = st.button("Search",use_container_width=True, key="Searchbutton1")
    if start_button:
        if tid:
            result = user_input_menu(tid)
            st.write(result)
            st.toast("Task completed successfully.")
        elif mtid:
            result = multi_user_input_menu(mtid)
            st.write(result)
            st.toast("Task completed successfully.")
        elif locid:
            tid = process_locid(locid)
            result = user_input_menu(tid)
            st.write(result)
            st.toast("Task completed successfully.")
        elif mlocid:
            mtid = process_mlocid(mlocid)
            result = multi_user_input_menu(mtid)
            st.write(result)
            st.toast("Task completed successfully.")
        else:
            st.warning("Need either a Gene ID or NCBI ID to proceed.")
    elif tid == "":
        st.warning("Need Gene ID/ NCBI ID to proceed.")
    else:
        st.write("Press the 'Start' button to begin the search.")
        st.write("Follow the instructions or check out tutorials")
    base_footer()

#if __name__ == "__main__":
#    search_page()
import streamlit as st
from pages.security_login import *
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'current_interface' not in st.session_state:
    st.session_state.current_interface = None

def clear_register_inputs():
    st.session_state.register_username1 = ""
    st.session_state.register_password1 = ""
    st.session_state.register_password2 = ""
    st.session_state.register_fname = ""
    st.session_state.register_lname = ""
    st.session_state.register_email1= ""

def clear_login_inputs():
    st.session_state.login_username = ""
    st.session_state.login_password = ""

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
            password = st.text_input("Password",key="login_password", type="password", label_visibility="collapsed")
        
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1,1,1,2,1,1,1])
        #with col4:
            #if st.button("Clear", use_container_width=True):
                #clear_login_inputs()
                #st.warning("Credentials Input cleared")
        with col4:
            if st.button("Continue", use_container_width=True):
                st.success("Chekcing credentials")
                if check_user(username, password):
                    st.session_state['authenticated'] = True
                    st.success("Logged in successfully!")
                    st.title(f"Welcome user")
                    conn = connect_to_db()
                    cursor = conn.cursor()
                    #main part to confirm
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
                    st.rerun()

                else:
                    st.error("Invalid username or password")

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
        
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1,1,1,2,1,1,1])
        #with col4:
            #if st.button("Clear", use_container_width=True):
                #clear_register_inputs()
                #st.warning("All inputs cleared!")
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
                
def authentication_flow():
    if st.session_state.authenticated:
        search_page()
        return

    st.title("Security")

    choice = st.radio("Choose an option:", ["Login", "Register"], index=0 if st.session_state.current_interface == "Login" else 1)

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

    st.session_state.current_interface = choice

    if st.session_state.current_interface == "Login":
        login_interface()
    elif st.session_state.current_interface == "Register":
        register_interface()
if __name__ == "__main__":
    authentication_flow()
