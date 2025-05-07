import streamlit as st
from pages.footer_all import base_footer 
from backend import generate_signed_url

@st.cache_data(show_spinner=False)
def get_image_url(image_path):
    return generate_signed_url(image_path)

def about_page():
    st.title("About Us")
    col1,col2=st.columns(2)
    st.markdown("""<style>.stVerticalBlock.st-key-au1 {background-color: rgb(185,214,148); color: white; padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-au1:hover {background-color: rgba(242,240,239,0.5); color: black; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    con=col1.container(border=False, key="au1")
    with con:
        c1,c2=st.columns([7,13])
        c1.image(get_image_url("About/img.jpg"),use_container_width=True)
        c2.subheader("Person1")
        c2.write("Hello")
    
    st.markdown("""<style>.stVerticalBlock.st-key-au2 {background-color: rgb(185, 214, 148); color: white; padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-au2:hover {background-color: rgba(242,240,239,0.5); color: black; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    con=col2.container(border=False, key="au2")
    with con:
        c1,c2=st.columns([7,13])
        c1.image(get_image_url("About/img.jpg"),use_container_width=True)
        c2.subheader("Person2")
        c2.write("Hello")

    #col1,col2=st.columns(2)
    st.markdown("""<style>.stVerticalBlock.st-key-au3 {background-color: rgb(185, 214, 148); color: white; padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-au3:hover {background-color: rgba(242,240,239,0.5); color: black; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    con=col1.container(border=False, key="au3")
    with con:
        c1,c2=st.columns([7,13])
        c1.image(get_image_url("About/img.jpg"),use_container_width=True)
        c2.subheader("Person3")
        c2.write("Hello")
    st.markdown("""<style>.stVerticalBlock.st-key-au4 {background-color: rgb(185, 214, 148); color: white; padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-au4:hover {background-color: rgba(242,240,239,0.5); color: black; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    con=col2.container(border=False, key="au4")
    with con:
        c1,c2=st.columns([7,13])
        c1.image(get_image_url("About/img.jpg"),use_container_width=True)
        c2.subheader("Person4")
        c2.write("Hello")

    #col1,col2=st.columns(2)
    st.markdown("""<style>.stVerticalBlock.st-key-au5 {background-color: rgb(185, 214, 148); color: white; padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-au5:hover {background-color: rgba(242,240,239,0.5); color: black; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    con=col1.container(border=False, key="au5")
    with con:
        c1,c2=st.columns([7,13])
        c1.image(get_image_url("About/img.jpg"),use_container_width=True)
        c2.subheader("Person5")
        c2.write("Hello")
    
    st.markdown("""<style>.stVerticalBlock.st-key-au6 {background-color: rgb(185, 214, 148); color: white; padding: 20px; border-radius: 10px; transition: all 0.3s ease-in-out;} .stVerticalBlock.st-key-au6:hover {background-color: rgba(242,240,239,0.5); color: black; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); transform: translateY(-2px);} </style>""", unsafe_allow_html=True)
    con=col2.container(border=False, key="au6")
    with con:
        c1,c2=st.columns([7,13])
        c1.image(get_image_url("About/img.jpg"),use_container_width=True)
        c2.subheader("Person6")
        c2.write("Hello")

    base_footer()

if __name__ == "__main__":
    about_page()
