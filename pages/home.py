import streamlit as st
from streamlit.components.v1 import html

def home_html():
    html_home_page="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <style>
        /* General Styles */
        .hp-body {
          font-family: Arial, sans-serif;
          margin: 0;
          padding: 0;
          background-color: #f4f4f9;
          color: #333;
        }

        .hp-container {
          max-width: 1000px;
          margin: 0 auto;
          padding: 20px;
          border-radius: 2rem;
        }

        /* Heading Styles */
        .hp-heading {
          text-align: center;
          font-size: 3.5rem;
          margin-bottom: 10px;
          color: #2c3e50;
        }

        .hp-subheading {
          text-align: center;
          font-size: 1.2rem;
          color: #7f8c8d;
          margin-bottom: 30px;
        }

        /* Paragraph Styles */
        .hp-paragraph {
          font-size: 1rem;
          line-height: 1.6;
          margin-bottom: 20px;
        }

        .hp-paragraph b {
          color: #e74c3c;
          font-weight: bold;
        }

        .hp-paragraph em {
          font-style: italic;
          text-decoration: underline;
        }

        .hp-list {
          list-style-type: square;
          margin-left: 20px;
        }

        /* Additional Paragraphs */
        .hp-additional-paragraph {
          font-size: 1rem;
          line-height: 1.6;
          margin-bottom: 30px;
        }
      </style>
    </head>
    <body class="hp-body">
      <div class="hp-container">
        <!-- Heading and Subheading -->
        <h1 class="hp-heading">Chickpea</h1>
        <h2 class="hp-subheading">OMICS EXPLORER</h2>

        <!-- Paragraph with List and Special Effects -->
        <p class="hp-paragraph">
          This is a <b>creative</b> paragraph showcasing some <em>special effects</em>. Here’s an unordered list of ideas:
        </p>
        <ul class="hp-list">
          <li>Dynamic Images</li>
          <li>Bold Text</li>
          <li>Images</li>
        </ul>

        <!-- Additional Paragraphs -->
        <p class="hp-additional-paragraph">
        Hello ...
        </p>
        <p class="hp-additional-paragraph">
          Hello ... <b>bold text</b> and <em>italicized text</em>...
        </p>

        <!-- More Text -->
        <p class="hp-additional-paragraph">
          hello ...
        </p>
      </div>

      
    </body>
    </html>"""

    html(html_home_page,height=500,scrolling=False)
    return

home_html()
