import streamlit as st
from pages.footer_all import base_footer 
from pages.home import home_html
from pages.gallery import gallery_html

def home_page():
    home_html()

    col1,col2=st.columns(2)
    st.markdown("""<style>.stVerticalBlock.st-key-con11hp {background-color: rgba(1,171,228,1); padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-con11hp:hover {background-color: rgba(1,171,228,0.5); box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    con=col1.container(border=True,key="con11hp")
    with con:
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
    con=col2.container(border=True,key="con12hp")
    st.markdown("""<style>.stVerticalBlock.st-key-con12hp {background-color: rgba(255,255,205,1); padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-con12hp:hover {background-color: rgba(255,255,205,0.5); box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
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
    st.markdown("""<style>.stVerticalBlock.st-key-con2hp {background-color: rgba(242,240,239,1); padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-con2hp:hover {background-color: rgba(242,240,239,0.5); box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    con=st.container(border=True,key="con2hp")
    with con:
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")

    col1,col2=st.columns(2)
    st.markdown("""<style>.stVerticalBlock.st-key-con31hp {background-color: rgba(195,216,161,1); padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-con31hp:hover {background-color: rgba(195,216,161,0.5); box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    con=col1.container(border=True,key="con31hp")
    with con:
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
        st.write(".")
    st.markdown("""<style>.stVerticalBlock.st-key-con32hp {background-color: rgba(255,119,75,1); padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-con32hp:hover {background-color: rgba(255,119,75,0.5); box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
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
