import folium
import io

def create_map_html(lat=45.5236,long=-122.6750,zoom=13):
    map = folium.Map(location=[lat, long], zoom_start=zoom)
    map.save('/map_src/templates/map.html')

def create_map_io(lat=45.5236,long=-122.6750,zoom=13):
    map = folium.Map(location=[lat, long], zoom_start=zoom)
    data = io.BytesIO()
    map.save(data,close_file=False)
    return data.getvalue().decode()