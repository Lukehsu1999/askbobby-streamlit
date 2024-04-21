import folium
import streamlit as st
import json
from streamlit_folium import st_folium
from folium.plugins import TimestampedGeoJson 
import random
import time
# checkout reference here: https://python-visualization.github.io/folium/latest/user_guide/plugins/message_timetamped_geojson.html

col1, col2 = st.columns([7,3])

with col1:
    st.header("Real-time AskBobby Requests")
    points = [
        # Existing points
        {"message_time": "2024-04-20T08:00:00", "type": "Food", "coordinates": [-73.935242, 40.730610]},  # Near Central Park
        {"message_time": "2024-04-20T08:01:00", "type": "Shelter", "coordinates": [-74.0060, 40.7128]},  # Statue of Liberty
        {"message_time": "2024-04-20T08:03:00", "type": "Health", "coordinates": [-73.935242, 40.8491]},  # Near Bronx Zoo
        {"message_time": "2024-04-20T08:05:00", "type": "Food", "coordinates": [-73.9981, 40.7328]},  # Washington Square Park
        {"message_time": "2024-04-20T08:07:00", "type": "Shelter", "coordinates": [-73.9776, 40.7536]},  # Grand Central Terminal
        {"message_time": "2024-04-20T08:10:00", "type": "Education", "coordinates": [-73.9619, 40.8075]},  # Near Columbia University
        {"message_time": "2024-04-20T08:15:00", "type": "Entertainment", "coordinates": [-73.9851, 40.7589]},  # Times Square
        {"message_time": "2024-04-20T08:20:00", "type": "Health", "coordinates": [-73.9680, 40.7612]},  # Near Rockefeller Center
        {"message_time": "2024-04-20T08:25:00", "type": "Food", "coordinates": [-73.9493, 40.6892]},  # Near Brooklyn Botanic Garden
        {"message_time": "2024-04-20T08:30:00", "type": "Shelter", "coordinates": [-73.9934, 40.7505]},  # Penn Station
        {"message_time": "2024-04-20T08:35:00", "type": "Shopping", "coordinates": [-74.0139, 40.7021]},  # Near Battery Park
        {"message_time": "2024-04-20T08:40:00", "type": "Culture", "coordinates": [-73.9732, 40.7794]},  # Near American Museum of Natural History
        {"message_time": "2024-04-20T08:45:00", "type": "Recreation", "coordinates": [-74.0445, 40.6892]},  # Statue of Liberty
        
        # New points in Brooklyn
        {"message_time": "2024-04-20T08:50:00", "type": "Culture", "coordinates": [-73.9927, 40.6612]},  # Prospect Park
        {"message_time": "2024-04-20T08:55:00", "type": "Food", "coordinates": [-73.9580, 40.6752]},  # Near Brooklyn Museum
        {"message_time": "2024-04-20T09:00:00", "type": "Health", "coordinates": [-73.9738, 40.6469]},  # Near Brooklyn Hospital Center
        
        # New points in Queens
        {"message_time": "2024-04-20T09:05:00", "type": "Shelter", "coordinates": [-73.8574, 40.7498]},  # Near Queens Center Mall
        {"message_time": "2024-04-20T09:10:00", "type": "Education", "coordinates": [-73.9415, 40.7433]},  # Near Queens College
        {"message_time": "2024-04-20T09:15:00", "type": "Entertainment", "coordinates": [-73.8448, 40.7216]},  # Flushing Meadows Corona Park
    ]



    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": point["coordinates"],
            },
            "properties": {
                "time": point["message_time"],
                "popup": point["type"]
            },
        }
        for point in points
    ]

    containers_map = folium.Map(location=[40.7057, -73.9262], zoom_start=11)
    TimestampedGeoJson(
        {"type": "FeatureCollection", "features": features},
        period="PT30S",
        add_last_point=True,
        duration="PT10M",
        ).add_to(containers_map)

    st_data = st_folium(containers_map)

with col2:
    with st.container():
        st.header("Top Requested Services:")

        # Define a list of services and initial counts
        services = {
            "Food": 100,
            "Shelter": 90,
            "Health": 80,
            "Education": 70,
            "Entertainment": 60
        }

        # Function to simulate receiving new requests
        def update_requests(services):
            """Randomly increase service requests to simulate new data."""
            return {service: count + random.randint(1, 10) for service, count in services.items()}

        # Function to generate sorted services by request count
        def generate_sorted_services(services):
            return sorted(services.items(), key=lambda item: item[1], reverse=True)

        # Create a placeholder for displaying the service ranking
        ranking_container = st.empty()

        # # Main loop for the dynamic dashboard
        # run_updates = True
        # while run_updates:
        #     # Update service counts
        #     services = update_requests(services)

        #     # Clear the previous content
        #     ranking_container.empty()

        #     # Generate sorted services and update the display
        #     sorted_services = generate_sorted_services(services)
        #     with ranking_container.container():
        #         for service, count in sorted_services:
        #             st.write(f"{service}: {count}")
                
        #     # Simulate a variable delay to mimic live updates
        #     sleep_duration = random.uniform(0.5, 1.5)
        #     time.sleep(sleep_duration)

    
    with st.container():
        st.header("Feedback livestream:")
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

        # Create a placeholder for live comments
        feedback_container = st.empty()

        # Introduce a variable to control the loop
        run_feedback = True

        # # Use a button to start the feedback loop
        # while run_feedback:
        #     new_feedback = generate_feedback()
        #     feedback_container.empty()  # Clear previous comments
        #     feedback_container.write(new_feedback)  # Display new feedback
                
        #     sleep_duration = random.uniform(0.5, 1.5)
        #     time.sleep(sleep_duration)
    run_updates = True
    while run_updates:
        # Update service counts
        services = update_requests(services)

        # Clear the previous content
        ranking_container.empty()

        # Generate sorted services and update the display
        sorted_services = generate_sorted_services(services)
        with ranking_container.container():
            for service, count in sorted_services:
                st.write(f"{service}: {count}")
        
        new_feedback = generate_feedback()
        feedback_container.empty()  # Clear previous comments
        feedback_container.write(new_feedback)  # Display new feedback
        
        # Simulate a variable delay to mimic live updates
        sleep_duration = random.uniform(0.5, 1.5)
        time.sleep(sleep_duration)           