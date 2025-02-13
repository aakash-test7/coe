import streamlit as st
from backend import user_input_menu, multi_user_input_menu, process_locid, process_mlocid
from pages.footer_all import base_footer
import time

def search_page():
    st.title("Search")
    st.write("**Begin the search by interacting with the backend process.**")
    col1, col2 = st.columns(2)

    with col1:
        con1 = st.container(border=True)
        tid = con1.text_input("Enter the Gene ID: ", placeholder="e.g., Ca_00001", key="Tid_input1").strip()
        mtid = con1.text_input("Enter multiple Gene IDs: ", placeholder="e.g., Ca_00001, Ca_00002", key="mTid_input2").strip()
        if mtid:
            mtid_list = [item.strip() for item in mtid.replace(",", " ").split()]
            mtid_list = list(set(mtid_list))
            mtid = ",".join(mtid_list)

    with col2:
        con2 = st.container(border=True)
        locid = con2.text_input("Enter the NCBI ID: ", placeholder="e.g., LOC101511858", key="Locid_input1").strip()
        mlocid = con2.text_input("Enter multiple NCBI IDs: ", placeholder="e.g., LOC101511858, LOC101496413", key="mLocid_input2").strip()
        if mlocid:
            mlocid_list = [item.strip() for item in mlocid.replace(",", " ").split()]
            mlocid_list = list(set(mlocid_list))
            mlocid = ",".join(mlocid_list)

    con1, con2, con3 = st.columns([2, 2, 2])
    with con2:
        start_button = st.button("Search", use_container_width=True, key="Searchbutton1")

    if start_button:
        if not st.session_state.get("logged_in", False):
            if tid or mtid or locid or mlocid:
                st.warning("You need to login to perform this action. Redirecting to login page in 5 seconds...")
                time.sleep(5)
                st.session_state["redirect_to_login"] = True
                st.rerun()
        else:
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
