import streamlit as st
from pages.footer_all import base_footer 

def about_page():
    st.title("About Us")
    st.write("**Learn more about the application and its developers.**")

    import urllib.parse
    with st.popover('Contact Us'):
        email_to = "gopalkalwan56@gmaill.com"
        subject = "MultiClassClassificationInput App Inquiry"
        body = "I am writing to inquire about..."
        subject_encoded = urllib.parse.quote(subject)
        body_encoded = urllib.parse.quote(body)
        mailto_link = f"mailto:{email_to}?subject={subject_encoded}&body={body_encoded}"
        st.markdown(f"[Tap the link to open E-mail](mailto:{email_to}?subject={subject_encoded}&body={body_encoded})")
    base_footer()

if __name__ == "__main__":
    about_page()
