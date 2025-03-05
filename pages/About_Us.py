import streamlit as st
from pages.footer_all import base_footer 
from pages.about_us_html import about_us_html

def about_page():
    about_us_html()
    base_footer()

if __name__ == "__main__":
    about_page()
