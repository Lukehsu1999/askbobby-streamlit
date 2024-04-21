import streamlit as st
import random
import time

sample_comments = [
    "This is awesome!",
    "Really enjoying the presentation so far.",
    "What software are you using for this?",
    "Can you explain that last part again?",
    "Great session, very informative!",
    "I love the visuals!",
    "The audio is a bit unclear.",
    "Thanks for this livestream!"
]

def generate_feedback():
    return random.choice(sample_comments)

st.title("Livestream Feedback Simulator")

# Create a placeholder for live comments
feedback_container = st.empty()

# Introduce a variable to control the loop
run_feedback = True

# Use a button to start the feedback loop
if st.button('Start', key='start_button'):
    while run_feedback:
        new_feedback = generate_feedback()
        feedback_container.empty()  # Clear previous comments
        feedback_container.write(new_feedback)  # Display new feedback
        
        sleep_duration = random.uniform(0.5, 1.0)
        time.sleep(sleep_duration)
        
