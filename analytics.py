import folium
import streamlit as st
import json
from streamlit_folium import st_folium
from folium.plugins import TimestampedGeoJson 
import random
import time
# checkout reference here: https://python-visualization.github.io/folium/latest/user_guide/plugins/message_timetamped_geojson.html

st.header("Bobby Analytics")
col1, col2 = st.columns([6,4])

with col1:
    st.subheader("Real-time AskBobby Requests")
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

    with st.container(border=True):
        st.subheader("Services Requested:")

        # Define a list of services and initial counts
        services = {
            "Food": 100,
            "Shelter": 95,
            "Health": 90,
            "Clothing": 70
        }

        # Function to simulate receiving new requests
        def update_requests(services):
            """Randomly increase service requests to simulate new data."""
            return {service: count + random.randint(0, 10) for service, count in services.items()}

        # Function to generate sorted services by request count
        def generate_sorted_services(services):
            return sorted(services.items(), key=lambda item: item[1], reverse=True)

        # Create a placeholder for displaying the service ranking
        ranking_container = st.empty()

    with st.container(border=True):
        st.subheader("Languages used")
        languages = {
            "English": 100,
            "Spanish": 103,
            "Chinese": 30,
            "Russian": 15
        }
        def update_languages(languages, lang):
            languages[lang] += 1
            return languages

        # Function to generate sorted services by request count
        def generate_sorted_languages(languages):
            return sorted(languages.items(), key=lambda item: item[1], reverse=True)
        
        language_container = st.empty()

    with st.container(border=True):
        st.subheader("Feedback livestream:")
        sample_comments = [
            {"message": "Im on a low carbohydrate high protein, no sugar or grains diet. We do not want preservatives, high fructose corn syrup etc in our food. We prefer fresh food , not canned.", "lang": "English"},
            {"message": "I would like to see more fresh fruits and vegetables at the pantry.", "lang": "English"},
            {"message": "鸡蛋,牛奶,新鲜蔬菜水果和鱼,牛肉,猪肉", "lang": "Chinese"},
            {"message": "Cultural Food to me represent the traditions, beliefs, and practices of a geographic region, ethnic group, religious body, or cross-cultural community.", "lang": "English"},
            {"message": "可以多一点蔬菜水果,不喜欢罐头制品", "lang": "Chinese"},
            {"message": "Thank you so much for all the work you guys do it's really much appreciated. God Bless and stay safe.", "lang": "English"},
            {"message": "I like very much how I can enter into the building and order and pick up my food in a organized and timely manner", "lang": "English"},
            {"message": "Me siento muy agradecida por esta ayuda ya q es muy importante para mí grupo familiar, ya que actualmente no poseemos empleo y de verdad gracias a ustedes hemos podido solucionar con esta ayuda", "lang": "Spanish"},
            {"message": "CAN VOLUNTEERS BE FROM OUR COMMUNITY? IT WOULD HELP THE NEIGHBORHOOD", "lang": "English"},
            {"message": "Gracipor el servicios que nos brindan para mi es como agua en el desierto, Dios le bendiga y nos provee el pan de cada días", "lang": "Spanish"},
            {"message": "Looks like every week new rules, Tuesday and Thursday are seniors but now anyone is available to get food between 930am and 11am in those days. Only 50 boxes given out each day. For 2 months I did not get a box. I had a low number but folks in the other line got boxes. One week sign said Seniors but non seniors on line and was served. Please set one set of rules. Before there would be 2 lines or non seniors at the end of line. Thank you", "lang": "English"},
            {"message": "Thank for helping", "lang": "English"},
            {"message": "Shower areas at NY Common Pantry need cleaning and disinfectant spray. Dignify this great resources", "lang": "English"},
            {"message": "Спасибо Вам большое, большая помощь. Удачи Вам в добрых делах", "lang": "Russian"},
            {"message": "粮食券发放时要严格严谨调查发放对象的条件和标准,不要辜负政府和NGO组织。", "lang": "Chinese"},
            {"message": "I am so greatful to the different pantry. I visit when I can and I also volunteer when necessary. Some visits are better than other times, but you always can get something that you could prepare a meal for your family even if you have to buy some type of poultry. At times when I get excess I share with my older neighbors. I am so appreciative to God our provider through many organizations. Thanks to all.", "lang": "English"},
            {"message": "Thanks for supporting", "lang": "English"},
            {"message": "Food bank for New York City has been a lifesaver", "lang": "English"},
            {"message": "Хотела бы ещё добавить, чтобы чаще было мясо, молоко, яйца", "lang": "Russian"}
        ]

        def generate_feedback():
            random_entry = random.choice(sample_comments)
            return random_entry["message"], random_entry["lang"]

        # Create a placeholder for live comments
        feedback_container = st.empty()
    
    run_updates = True
    while run_updates:
        # Update service counts
        services = update_requests(services)

        # Clear the previous content
        ranking_container.empty()

        # Generate sorted services and update the display
        service_color = {
            "Food": "#007bff",
            "Shelter": "#28a745",
            "Health": "#dc3545",
            "Clothing": "#fd7e14"
        }
        sorted_services = generate_sorted_services(services)
        with ranking_container.container():
            for service, count in sorted_services:
                card_html = f"""
                <div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0; border-radius: 5px; color: white; background-color: {service_color.get(service, '#6c757d')}">
                    <strong>{service}:</strong> {count}
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
        
        new_feedback, lang = generate_feedback()
        feedback_container.empty()  # Clear previous comments
        feedback_container.write(new_feedback)  # Display new feedback

        # Update language counts
        language_color = {
            "English": "#007bff",  # Blue
            "Spanish": "#28a745",  # Green
            "Chinese": "#dc3545",  # Red
            "Russian": "#fd7e14"  # Orange
        }

        language_container.empty()  # Placeholder for dynamic content
        languages = update_languages(languages, lang)
        sorted_languages = generate_sorted_languages(languages)
        with language_container.container():
            for language, count in sorted_languages:
                # Using Markdown to create a colored card for each language
                card_html = f"""
                <div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0; border-radius: 5px; color: white; background-color: {language_color.get(language, '#6c757d')}">
                    <strong>{language}:</strong> {count}
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)

        
        # Simulate a variable delay to mimic live updates
        sleep_duration = random.uniform(0.5, 1.5)
        time.sleep(sleep_duration)           