import folium
import streamlit as st
import json
from streamlit_folium import st_folium
from folium.plugins import TimestampedGeoJson 
# checkout reference here: https://python-visualization.github.io/folium/latest/user_guide/plugins/message_timetamped_geojson.html

points = [
    {"message_time": "2024-04-20T08:00:00", "type": "Food", "coordinates": [-73.935242, 40.730610]},  # Near Central Park
    {"message_time": "2024-04-20T08:01:00", "type": "Shelter", "coordinates": [-74.0060, 40.7128]},  # Statue of Liberty
    {"message_time": "2024-04-20T08:03:00", "type": "Health", "coordinates": [-73.935242, 40.8491]},  # Near Bronx Zoo
    {"message_time": "2024-04-20T08:05:00", "type": "Food", "coordinates": [-73.9981, 40.7328]},  # Washington Square Park
    {"message_time": "2024-04-20T08:07:00", "type": "Shelter", "coordinates": [-73.9776, 40.7536]},  # Grand Central Terminal
    # Adding new data points
    {"message_time": "2024-04-20T08:10:00", "type": "Education", "coordinates": [-73.9619, 40.8075]},  # Near Columbia University
    {"message_time": "2024-04-20T08:15:00", "type": "Entertainment", "coordinates": [-73.9851, 40.7589]},  # Times Square
    {"message_time": "2024-04-20T08:20:00", "type": "Health", "coordinates": [-73.9680, 40.7612]},  # Near Rockefeller Center
    {"message_time": "2024-04-20T08:25:00", "type": "Food", "coordinates": [-73.9493, 40.6892]},  # Near Brooklyn Botanic Garden
    {"message_time": "2024-04-20T08:30:00", "type": "Shelter", "coordinates": [-73.9934, 40.7505]},  # Penn Station
    {"message_time": "2024-04-20T08:35:00", "type": "Shopping", "coordinates": [-74.0139, 40.7021]},  # Near Battery Park
    {"message_time": "2024-04-20T08:40:00", "type": "Culture", "coordinates": [-73.9732, 40.7794]},  # Near American Museum of Natural History
    {"message_time": "2024-04-20T08:45:00", "type": "Recreation", "coordinates": [-74.0445, 40.6892]},  # Statue of Liberty
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

containers_map = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
TimestampedGeoJson(
    {"type": "FeatureCollection", "features": features},
    period="PT15S",
    add_last_point=True,
    duration="PT10M",
    ).add_to(containers_map)

st_data = st_folium(containers_map)