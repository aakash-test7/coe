import streamlit as st
from pages.footer_all import base_footer 
from pages.home import home_html
from pages.gallery import gallery_html

def home_page():
    home_html()

    col1,col2=st.columns(2)
    st.markdown("""<style>.stVerticalBlock.st-key-con11hp {background-color: #DAF7A6; padding: 20px; border-radius: 10px;} </style>""", unsafe_allow_html=True)
    con=col1.container(border=True,key="con11hp")
    with con:
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
    con=col2.container(border=True,key="con12hp")
    st.markdown("""<style>.stVerticalBlock.st-key-con12hp {background-color: #F1F7A6; padding: 20px; border-radius: 10px;} </style>""", unsafe_allow_html=True)
    with con:
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")

    con=st.container(border=True)
    with con:
        gallery_html()

    con=st.container(border=True,key="con2hp")
    with con:
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")

    col1,col2=st.columns(2)
    st.markdown("""<style>.stVerticalBlock.st-key-con31hp {background-color: #DAF7A6; padding: 20px; border-radius: 10px;} </style>""", unsafe_allow_html=True)
    con=col1.container(border=True,key="con31hp")
    with con:
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
    st.markdown("""<style>.stVerticalBlock.st-key-con32hp {background-color: #F1F7A6; padding: 20px; border-radius: 10px;} </style>""", unsafe_allow_html=True)
    con=col2.container(border=True,key="con32hp")
    with con:
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")

    base_footer()

if __name__ == "__main__":
    home_page()
