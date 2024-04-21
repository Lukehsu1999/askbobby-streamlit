import streamlit as st
import json

col1, col2 = st.columns([7,3])

custom_css = """
<style>
div.stContainer {
    background-color: #f0f2f6;
    border: 2px solid #e1e4e8;
    border-radius: 10px;
    padding: 10px;
    margin-top: 5px;
    box-shadow: 5px 5px 5px rgba(0,0,0,0.1);
}
</style>
"""

with col1:
    st.header("Funding Programs based on Bobby's suggestions")
    # Define data for multiple rows of cards
data = [
    {"title": "Card 1", "description": "This is card 1 in row 1"}, 
     {"title": "Card 2", "description": "This is card 2 in row 1"},
    {"title": "Card 3", "description": "This is card 1 in row 2"}, 
     {"title": "Card 4", "description": "This is card 2 in row 2"}
]

# Loop through each row of cards
for card in data:
    st.subheader(card["title"])
    st.write(card["description"])
    if st.button("Click Me", key=f"{card['title']}"):
        st.success(f"You clicked on {card['title']}!")

with col2:
    st.header("Federal Tax deduction calculator")