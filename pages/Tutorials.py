import streamlit as st
from backend import generate_signed_url
from pages.footer_all import base_footer

# ✅ Cache the video URL generation to avoid repeated calls
@st.cache_data(show_spinner=False)
def get_video_url(video_path):
    return generate_signed_url(video_path)

def tutorials_page():
    st.title("Tutorials Page")
    st.write("**Learn how to use this interface**")
    st.write("This page helps you understand how to use the app through video tutorials. Follow the steps below:")

    # ✅ Cache the video URLs for tutorials
    navigation_video_url = get_video_url("Videos/navigation.mp4")
    if navigation_video_url:
        st.video(navigation_video_url, start_time=0)
    else:
        st.warning("Video not found or unable to generate URL.")

    st.subheader("Registration and Login")
    register_video_url = get_video_url("Videos/register.mp4")
    if register_video_url:
        st.video(register_video_url, start_time=0)
    else:
        st.warning("Video not found or unable to generate URL.")
    st.markdown("""
    1. Navigate to the Login page.
    2. Register for new users.
    3. Login using your credentials.
    4. Unlock Search functionality and additional features.""")

    st.subheader("Single Task Tutorial")
    start_task1_video_url = get_video_url("Videos/start_task1.mp4")
    if start_task1_video_url:
        st.video(start_task1_video_url, start_time=0)
    else:
        st.warning("Video not found or unable to generate URL.")
    st.markdown("""
    1. Navigate to the **Start Task** page.
    2. Enter the 8-character code when prompted.
    3. Click the **Start** button to begin the task.
    4. Wait for the task to complete and view the results.""")

    st.subheader("Multi Task Tutorial")
    start_task2_video_url = get_video_url("Videos/start_task2.mp4")
    if start_task2_video_url:
        st.video(start_task2_video_url, start_time=0)
    else:
        st.warning("Video not found or unable to generate URL.")
    st.markdown("""
    1. Navigate to the **Start Task** page.
    2. Enter the 8-character code when prompted.
    3. Click the **Start** button to begin the task.
    4. Wait for the task to complete and view the results.""")

    st.subheader("Glossary Tutorial")
    glossary_video_url = get_video_url("Videos/glossary.mp4")
    if glossary_video_url:
        st.video(glossary_video_url, start_time=0)
    else:
        st.warning("Video not found or unable to generate URL.")

    # Call base_footer function
    base_footer()

if __name__ == "__main__":
    tutorials_page()
