import folium
import streamlit as st
import json
from streamlit_folium import st_folium
from folium.plugins import TimestampedGeoJson 
# checkout reference here: https://python-visualization.github.io/folium/latest/user_guide/plugins/timestamped_geojson.html


with open('timestamped_bobby_requests.geojson') as j:
    data = json.load(j)

containers_map = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
TimestampedGeoJson(data, period="PT30S",
    add_last_point=True,duration="PT1M",).add_to(containers_map)
# folium.Marker(
#     [40.7580, -73.9855],  # Latitude and Longitude of Times Square
#     popup="Times Square",  # Popup label that appears when you click on the marker
#     tooltip="Click for more info"  # Tooltip text that appears when you hover over the marker
# ).add_to(containers_map)
# call to render Folium map in Streamlit
st_data = st_folium(containers_map)