import streamlit as st
from backend import generate_signed_url, img_to_base64
import requests

def base_footer():
    file_url = generate_signed_url('Logos/mdu.png')
    response = requests.get(file_url)
    img_base64 = img_to_base64(response.content)
    footer_image = f"data:image/png;base64,{img_base64}"
    footer = f"""
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
    
        html, body {{
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
        }}
    
        body {{
            font-family: 'Poppins', sans-serif;
            background: #eef8ff;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }}
    
        main {{
            flex: 1;
        }}
    
        .footer-container {{
            width: 100%;
            background: #000000;
            color: #fff;
            position: bottom;
            bottom: 0;
            left: 0;
            padding: 0 0;  /* No horizontal padding */
            z-index: 9999; /* Ensures the footer is above other content */
            /*max-height: 280px;*/
        }}
    
        .container {{
            width: 100%;
            margin: 0;
            padding: 0 20px;  /* Horizontal padding for alignment */
            display: flex;
            justify-content: space-evenly;
            align-items: flex-start;
            flex-wrap: wrap;
        }}
    
        .container li a:hover {{
            color: #01e72b;
            transition: all 0.5s ease;
        }}
    
        .col-1 {{
            flex-basis: 50%;
            padding: 5px;
            margin-bottom: 20px;
        }}
    
        .col-1 img {{
            width: 55px;
            margin-bottom: 15px;
        }}
    
        .col-1 p {{
            color: #fff;
            font-size: 16px;
            line-height: 20px;
        }}
    
        .col-3 {{
            flex-basis: 15%;
            padding: 5px;
            margin-bottom: 2px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center; /* Ensure text is centered */
        }}
    
        .col-3 h3 {{
            color: #fff;
            font-size: 25px;
            margin-top: 10px;
            margin-bottom: 10px; /* Add spacing between h3 and image */
        }}
    
        .col-3 img {{
            width: 125px; /* Fixed width */
            height: auto; /* Maintain aspect ratio */
            min-width: 125px; /* Prevent shrinking */
        }}
    
        .container a {{
            color: #fff;
        }}
    
        .container a:hover {{
            color: #b9d694;
            transition: all 0.5s ease;
        }}
    
        .footer-2 {{
            width: 100%;
            background: #2d2d2d;
            color: #fff;
            padding-top: 12px;
            padding-bottom: 2px;
            text-align: center;
        }}
        
    </style>
    
    <div class="footer-container">
        <div class="container">
            <div class="col-1">
                <p><br><br><br>Stress Physiology & Molecular Biology Lab,<br>Centre for Biotechnology,<br>Maharshi Dayanand University, Rohtak, HR, INDIA<br>E-mail : <br><a href="mailto:ssgill14@mdurohtak.ac.in" style="text-decoration: none;">ssgill14@mdurohtak.ac.in</a><br>
            <a href="mailto:kduiet@mdurohtak.ac.in " style="text-decoration: none;">kduiet@mdurohtak.ac.in</a></p>
            </div>
            <div class="col-3">
                <h3><a href="https://mdu.ac.in/default.aspx" style="text-decoration: none;" target="_blank">MDU</a></h3>
                <img src="{footer_image}" alt="mdu">
            </div>
        </div>
        <div class="footer-2">
            <p style="font-size: 15px">ChickpeaOmicsExplorer</p>
        </div>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
    return

base_footer()
