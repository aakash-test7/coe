import streamlit as st
st.set_page_config(page_title="ChickpeaOmicsExplorer", layout="wide")

from streamlit_navigation_bar import st_navbar
import pages as pg

pages = ["Home", "Search", "Meta-Data", "Glossary", "Tutorials", "Citations", "About Us", "MDU","Login"]
logo_path = ("logo.svg")
urls = {"MDU": "https://mdu.ac.in/default.aspx"}

styles = {
    "nav": {
        "background-color": "rgb(185, 214, 148)",  # Background color of the navigation bar
        "height": "4rem",  # Set the total height of the navigation bar
        "display": "flex",  # Use flexbox for layout
        "align-items": "center",  # Vertically center the items
        "justify-content": "space-around",  # Spread out the headings evenly
        "padding": "0 1rem",  # Add padding to the left and right of the navigation bar
        "overflow-x": "auto",  # Enable horizontal scrolling if the content overflows
        "white-space": "nowrap",  # Prevent items from wrapping to a new line
    },
    "div": {
        "max-width": "72rem",  # Limit the maximum width of the navigation bar content
    },
    "span": {
        "border-radius": "0.5rem",  # Rounded corners for the headings
        "color": "rgb(49, 51, 63)",  # Text color of the headings
        "margin": "0 0.125rem",  # Margin around each heading
        "padding": "0.4375rem 0.625rem",  # Padding inside each heading
        "font-size": "1.1rem",  # Increase the font size of the headings
        "font-weight": "bold",  # Make the headings bold
        "text-transform": "uppercase",  # Convert heading text to uppercase
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",  # Background color for the active heading
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",  # Background color on hover
    },
}

# Inject custom CSS for mobile responsiveness
st.markdown("""
    <style>
        /* Mobile responsiveness */
        @media (max-width: 768px) {
            .stNavBar-nav {
                overflow-x: scroll;  /* Enable scrolling on smaller screens */
                flex-wrap: nowrap;    /* Prevent wrapping of items */
                padding: 0.5rem;      /* Adjust padding for mobile */
            }
            .stNavBar-span {
                font-size: 0.9rem;      /* Slightly reduce font size for mobile */
                padding: 0.375rem 0.5rem; /* Adjust padding for mobile screens */
            }
        }
    </style>
""", unsafe_allow_html=True)
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

page = st_navbar(pages, logo_path=logo_path, urls=urls, styles=styles)

if page != st.session_state.current_page:
    st.session_state.current_page = page

# Sidebar navigation
# st.sidebar.title("Navigation")
pages2 = ["Home", "Search", "Meta-Data", "Glossary", "Tutorials", "Citations", "About Us","Login"]

for page_name in pages2:
    if st.sidebar.button(page_name, use_container_width=True):
        st.session_state.current_page = page_name

# BUTTONS NAVIGATION
st.sidebar.markdown("---")  # Adds a separator
st.markdown(
    """
    <style>
        .sidebar-button, .stButton>button {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            color: black;
            background-color: #C3D8A1; /* Green */
            border: 2px solid #9CAD81;
            border-radius: 15px;
            cursor: pointer;
            margin-bottom: 5px;
            text-align: center;
            display: block;
            text-decoration: none;
            transition: all 0.3 ease;
        }

        .sidebar-button:hover, .stButton>button:hover {
            background-color: #ff774b; /* Darker Green */
            border-color: #2d2d2d;
        }

        .stButton>button:hover p {
            color: black !important; /* Keep text visible */
        }
    </style>
    """,
    unsafe_allow_html=True,
)
external_links = {
    "Google": "https://www.google.com",
    "GitHub": "https://github.com",
    "Streamlit": "https://streamlit.io"
}
for name, link in external_links.items():
    st.sidebar.markdown(
        f'<a href="{link}" target="_blank" class="sidebar-button">{name}</a>',
        unsafe_allow_html=True
    )
functions = {
    "Home": pg.home_page,
    "Search": pg.search_page,
    "Meta-Data": pg.meta_data_page,
    "Glossary": pg.glossary_page,
    "Tutorials": pg.tutorials_page,
    "Citations": pg.citations_page,
    "About Us": pg.about_page,
    "Login":pg.login_page
}

go_to = functions.get(st.session_state.current_page)
if go_to:
    go_to()
