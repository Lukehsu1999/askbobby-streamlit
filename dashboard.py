import streamlit as st
import random
import time

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

# Main loop for the dynamic dashboard
if st.button('Start Service Updates'):
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
        
        # Simulate a variable delay to mimic live updates
        sleep_duration = random.uniform(0.5, 1.5)
        time.sleep(sleep_duration)

