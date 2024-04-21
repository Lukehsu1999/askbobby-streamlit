import streamlit as st
import json

col1, col2 = st.columns([7,3])

with col1:
    st.header("Funding Programs based on Bobby's suggestions")
    # Define data for multiple rows of cards
    data = [
        {"title": "Food for East Harlem", "description": "Bobby received an increasing food requests in East Harlem area.", "icon_url":"https://cdn-icons-png.flaticon.com/512/1046/1046784.png"}, 
        {"title": "Refugees Health Fund", "description": "Bobby spotted a 120% increase in health requests from refugees in NYC.", "icon_url":"https://cdn-icons-png.flaticon.com/512/2875/2875419.png"},
        {"title": "Fresh food Program NYC", "description": "Based on 120+ user feedback, people are looking for fresh vegetables and fruits replacing canned foods"}, 
        {"title": "Building a new shelter @Greater South Bronx", "description": "Over the last 2 weeks, Bobby received 100+ requests for shelter in Greater South Bronx.", "icon_url":"https://cdn-icons-png.flaticon.com/512/854/854878.png"},
        {"title": "Spanish-speaking Volunteers needed @Queens", "description": "Food Pantries in Queens area reported a 30% increase in Spanish-speaking clients. Volunteers familiar with Spanish are needed."}
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
            <img src="{card.get('icon_url', 'https://cdn-icons-png.flaticon.com/512/1046/1046784.png')}" style="width: 50px; height: 50px; float: left; margin-right: 10px;">
            <h2>{card['title']}</h2>
            <p>{card['description']}</p>
            <button class='button' onclick="alert('Clicked {card['title']}!');">Donate</button>
        </div>

        """
        st.markdown(card_html, unsafe_allow_html=True)

with col2:
    st.header("Federal Tax deduction calculator")


with open('wave.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)