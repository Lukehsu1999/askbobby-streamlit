import streamlit as st
import time
import random

# Define a function to update the requests count
def update_requests(services):
    """Simulate data updates by randomly increasing service requests."""
    for service in services:
        services[service] += random.randint(1, 10)  # Random increment to simulate new requests
    return services

# Initialize or update the session state for services if not already set
if 'services' not in st.session_state:
    st.session_state.services = {
        "Food": 100,
        "Shelter": 90,
        "Health": 80,
        "Education": 70,
        "Entertainment": 60
    }

# Title and header of the dashboard
st.title("Service Request Dashboard")
st.header("Analytics: Top 5 requested services")

# Button to manually trigger updates
if st.button('Update Now'):
    st.session_state.services = update_requests(st.session_state.services)

# Display the services sorted by the number of requests (most requests on top)
sorted_services = sorted(st.session_state.services.items(), key=lambda x: x[1], reverse=True)
for service, count in sorted_services:
    st.write(f"{service}: {count}")

# Add a placeholder for future updates
placeholder = st.empty()

# Update the data every few seconds
while True:
    # Check if the loop should continue
    if 'keep_updating' in st.session_state and not st.session_state.keep_updating:
        break
    
    # Update the service data
    st.session_state.services = update_requests(st.session_state.services)
    sorted_services = sorted(st.session_state.services.items(), key=lambda x: x[1], reverse=True)

    # Update the display in the placeholder
    with placeholder.container():
        for service, count in sorted_services:
            st.write(f"{service}: {count}")

    # Sleep to slow down the updates for readability
    time.sleep(2)
