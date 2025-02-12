import streamlit as st
from pages.footer_all import base_footer 

def citations_page():
    st.title("Citations")
    con=st.container(border=True)
    con.subheader("Sources and citations used in the work :- ")
    con.write (".")
    con.write (".")
    con.write (".")
    base_footer() 



    return

if __name__=="__main__":
    citations_page()