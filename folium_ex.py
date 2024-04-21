import folium
import streamlit as st
import json
from streamlit_folium import st_folium
from folium.plugins import TimestampedGeoJson 

with open('smart_trash_containers.geojson') as j:
    data = json.load(j)

for i in range(len(data['features'])):
     data['features'][i]['properties']['times'] = [data['features'][i]['properties']['assignment_date'][:19]]

# center on Liberty Bell, add marker
# m = folium.Map(location=[39.949610, -75.150282], zoom_start=10)
# folium.Marker(
#     [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
# ).add_to(m)

containers_map = folium.Map(location=[40.4406, -79.9959], zoom_start=12)
TimestampedGeoJson(data, transition_time=300).add_to(containers_map)

# call to render Folium map in Streamlit
st_data = st_folium(containers_map, width=725)