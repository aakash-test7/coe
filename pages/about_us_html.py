import streamlit as st
from streamlit.components.v1 import html

def about_us_html():

    about_us_=f"""
    <style>
        /* Importing the Nunito font from Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@200;300;400;600;700&display=swap');
        
        /* Defining a CSS variable for the color orange */
        :root {{
          --orange: #bfd59b;/*#ffa500;*/
        }}
        
        /* Universal reset for all elements */
        * {{
          font-family: 'Nunito', sans-serif; /* Setting the default font to Nunito */
          margin: 0; /* Removing default margin */
          padding: 0; /* Removing default padding */
          box-sizing: border-box; /* Ensuring padding and border are included in element dimensions */
          outline: none; /* Removing default outline */
          border: none; /* Removing default border */
          text-decoration: none; /* Removing default text decoration (e.g., underline on links) */
          transition: all 0.2s linear; /* Adding a smooth transition effect for all properties */
        }}
        
        /* Styling for text selection */
        *::selection {{
          background: var(--orange); /* Setting the background color of selected text to orange */
          color: rgba(238,127,87,1); /* Setting the text color of selected text to white */
        }}
        
        /* Base styles for the HTML element */
        html {{
          font-size: 62.5%; /* Setting base font size to 10px (62.5% of 16px) */
          overflow-x: hidden; /* Hiding horizontal scrollbar */
          scroll-padding-top: 6rem; /* Adding padding to the top of scrollable areas */
          scroll-behavior: smooth; /* Enabling smooth scrolling */
        }}
        
        /* Styling for all sections */
        section {{
          padding: 4rem 5%; /* Adding padding to all sections */
        }}
        
        /* Styling for headings */
        .heading{{
          text-align: center; /* Centering the heading text */
          padding: 4rem 0; /* Adding padding to the top and bottom of headings */
        }}
        
        /* Styling for the span inside headings */
        .heading span {{
          font-size: 3.5rem; /* Setting font size */
          border-radius: 0.5rem; /* Adding rounded corners */
          padding: 0.2rem 1rem; /* Adding padding */
        }}
      
        /* Styling for buttons */
        .btn {{
          display: inline-block; /* Making buttons inline-block elements */
          margin-top: 1rem; /* Adding margin to the top of buttons */
          background: var(--orange); /* Setting background color to orange */
          color: #fff; /* Setting text color to white */
          padding: 0.8rem 3rem; /* Adding padding */
          border: 0.2rem solid var(--orange); /* Adding a border */
          cursor: pointer; /* Changing cursor to pointer on hover */
          font-size: 1.7rem; /* Setting font size */
          border-radius: 0.5rem;
        }}
        
        /* Styling for button hover state */
        .btn:hover {{
          background: rgba(238,127,87,1); /* Changing background color on hover of gallery buttons */
          color: var(--orange); /* Changing text color on hover */
        }}
        
        /* Styling for the about-us section */
        .about-us .box-container {{
          display: flex; /* Using flexbox for layout */
          flex-wrap: wrap; /* Allowing items to wrap to the next line */
          gap: 1.5rem; /* Adding space between items */
        
        }}
        .about-us .box-container .box {{
          display: flex; /* Use flexbox layout */
          flex: 1 1 calc(50% - 1rem);
          align-items: center; /* Vertically center items */
          justify-content: flex-start; /* Align items to the start of the container */
          border-radius: 0.5rem; /* Adding rounded corners */
          padding: 1rem; /* Adding padding */
          text-align: left; /* Align text to the left */
          background: rgba(191, 213, 155, 0.2);
          
          
        }}
        /* Styling for individual boxes in the about-us section */
        .about-us .box-container .box {{
          border-radius: 0.5rem; /* Adding rounded corners */
          padding: 1rem; /* Adding padding */
          text-align: center; /* Centering text */
          background: rgba(191,213,155,0.2);
        
        }}
        /* Styling for images inside the boxes */
        .about-us .box-container .box img {{
          width: 40%; /* Set the image width to 40% */
          margin-right: 1rem; /* Add space between image and text */
          border-radius: 0.5rem;
        }}
        /* Styling for icons inside boxes */
        .about-us .box-container .box i {{
          padding: 1rem; /* Adding padding */
          font-size: 5rem; /* Setting icon size */
          color: var(--orange); /* Setting icon color to orange */
        }}
        
        /* Styling for headings inside boxes */
        .about-us .box-container .box h3 {{
          font-size: 2.5rem; /* Setting font size */
          color: #333; /* Setting text color */
        }}
        
        /* Styling for paragraphs inside boxes */
        .about-us .box-container .box p {{
          font-size: 1.5rem; /* Setting font size */
          color: #666; /* Setting text color */
          padding: 1rem 0; /* Adding padding */
          text-align: justify; /* Justifying text */
          text-justify: inter-word; /* Ensuring proper spacing between words */
        }}
        
        /* Styling for box hover state */
        .about-us .box-container .box:hover {{
          box-shadow: 1rem 1rem 0.5rem 0.5rem rgba(0, 0, 0, 0.4); /* Adding a shadow on hover */
        }}
        </style>
        
        
        <html lang="en">
        <head>
        
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
            
        </head>
        <body>
        
          <section class="about-us" id="about-us">
            <h1 class="heading">
                <span>About Us</span>
            </h1>
        
            <div class="box-container">
                <div class="box">
                    <img src="img.jpg" alt="" height="50%">
                    <div>
                        <h3>Person 1</h3>
                        <p>Person 1 ...</p>
                        <a href="mailto:akharbrtk2@gmail.com?subject=Chickpea%20Omics%20Explorer%20App%20Inquiry&body=I%20am%20writing%20to%20inquire%20about..." class="btn">E-mail</a>

                    </div>
                </div>
                <div class="box">
                    <i class="fas fa-user"></i>
                    <div>
                        <h3>Person 2</h3>
                        <p>Person 2 ...</p>
                        <a href="mailto:akharbrtk2@gmail.com?subject=Chickpea%20Omics%20Explorer%20App%20Inquiry&body=I%20am%20writing%20to%20inquire%20about..." class="btn">E-mail</a>

                    </div>
                </div>
                <div class="box">
                    <i class="fas fa-user"></i>
                    <div>
                        <h3>Person 3</h3>
                        <p>Person 3 ...</p>
                        <a href="mailto:akharbrtk2@gmail.com?subject=Chickpea%20Omics%20Explorer%20App%20Inquiry&body=I%20am%20writing%20to%20inquire%20about..." class="btn">E-mail</a>

                    </div>
                </div>
                <div class="box">
                    <i class="fas fa-user"></i>
                    <div>
                        <h3>Person 4</h3>
                        <p>Person 4 ...</p>
                        <a href="mailto:akharbrtk2@gmail.com?subject=Chickpea%20Omics%20Explorer%20App%20Inquiry&body=I%20am%20writing%20to%20inquire%20about..." class="btn">E-mail</a>

                    </div>
                </div>
                <div class="box">
                    <i class="fas fa-user"></i>
                    <div>
                        <h3>Person 5</h3>
                        <p>Person 5 ...</p>
                        <a href="mailto:akharbrtk2@gmail.com?subject=Chickpea%20Omics%20Explorer%20App%20Inquiry&body=I%20am%20writing%20to%20inquire%20about..." class="btn">E-mail</a>

                    </div>
                </div>
                <div class="box">
                    <i class="fas fa-user"></i>
                    <div>
                        <h3>Person 6</h3>
                        <p>Person 6 ...</p>
                        <a href="mailto:akharbrtk2@gmail.com?subject=Chickpea%20Omics%20Explorer%20App%20Inquiry&body=I%20am%20writing%20to%20inquire%20about..." class="btn">E-mail</a>

                    </div>
                </div>
            </div>
        </section>
        
        <!-- about-us section ends -->
                      
        </body>
        </html>
    """

    html(about_us_,height=800,scrolling=True)
    return

about_us_html()

