import streamlit as st
import json

col1, col2 = st.columns([7,3])

with col1:
    st.header("Funding Programs based on Bobby's suggestions")
    # Define data for multiple rows of cards
    data = [
        {"title": "Card 1", "description": "This is card 1 in row 1"}, 
        {"title": "Card 2", "description": "This is card 2 in row 1"},
        {"title": "Card 3", "description": "This is card 1 in row 2"}, 
        {"title": "Card 4", "description": "This is card 2 in row 2"}
    ]
    st.markdown("""
        <style>
        .card {
            background-color: #ffffff; /* White background */
            border: 2px solid #e1e4e8; /* Solid border with light gray color */
            border-radius: 10px; /* Rounded corners */
            padding: 10px; /* Padding inside the card */
            margin: 10px 0px; /* Margin outside the card */
            box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Subtle shadow around the card */
        }
        .button {
            display: block;
            width: 100%;
            padding: 8px;
            margin: 10px 0;
            background-color: #007BFF;
            color: white;
            text-align: center;
            border-radius: 5px;
            text-decoration: none;
        }
        </style>
        """, unsafe_allow_html=True)

    # Loop through each row of cards
    for card in data:
        # Create a full card's HTML content
        card_html = f"""
        <div class='card'>
            <h2>{card['title']}</h2>
            <p>{card['description']}</p>
            <button class='button' onclick="alert('Clicked {card['title']}!');">Click Me</button>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

with col2:
    st.header("Federal Tax deduction calculator")


with open('wave.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)