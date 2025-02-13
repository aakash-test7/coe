import streamlit as st
from backend import user_input_menu, multi_user_input_menu, process_locid, process_mlocid
from pages.footer_all import base_footer 

def show_login_popup():
    st.markdown(
        """
        <div style="background-color: lightgray; padding: 20px; border-radius: 10px;">
            <h3>Login Required</h3>
            <p>Please <a href='https://chickpea7.streamlit.app/~/+/component/streamlit_navigation_bar.st_navbar/index.html?streamlitUrl=https%3A%2F%2Fchickpea7.streamlit.app%2F~%2F%2B%2F#' target='_blank'>Login</a> to access more features.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
def search_page():
    st.title("Search")
    st.write("**Begin the search by interacting with the backend process.**")
    col1, col2 = st.columns(2)

    with col1:
        con1=st.container(border=True)
        tid = con1.text_input("Enter the Gene ID: ", placeholder="e.g., Ca_00001", key="Tid_input1").strip()
        if tid:
            show_login_popup()
        mtid = con1.text_input("Enter multiple Gene IDs: ", placeholder="e.g., Ca_00001, Ca_00002", key="mTid_input2").strip()
        if mtid:
            show_login_popup()

        if mtid:
            mtid_list = [item.strip() for item in mtid.replace(",", " ").split()]
            mtid_list = list(set(mtid_list))
            mtid = ",".join(mtid_list)

    with col2:
        con2=st.container(border=True)
        locid = con2.text_input("Enter the NCBI ID: ", placeholder="e.g., LOC101511858", key="Locid_input1").strip()
        if locid:
            show_login_popup()
        mlocid = con2.text_input("Enter multiple NCBI IDs: ", placeholder="e.g., LOC101511858, LOC101496413", key="mLocid_input2").strip()
        if mlocid:
            show_login_popup()
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

if __name__ == "__main__":
    search_page()
