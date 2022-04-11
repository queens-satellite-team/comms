import requests
from API_KEY import OWM_API_KEY
from tkinter import *


def get_open_weather_map_layer(OWM_API_KEY,layer:str='wind_new', z:str='0', x:str='0',y:str='0'):
    '''
        breif: Sends a request to the open weather weather map API and saves visual weather data as a jpg file in the
        project workspace. This file will be later inserted into tkinter using gui_builder.py

        param:
            OWM_API_KEY - the unique open weather api authentication key from API_KEY.py
            layer - specific weather map layer want to display. Options are: 
                    'clouds_new', 
                    'precipitation_new',
                    'pressure_new',
                    'wind_new',
                    'temp_new'
            z - number of zoom level,
            x - number of x tile coordinate,
            y - number of y tile coordinate.
    '''
    url = 'https://tile.openweathermap.org/map/{map_type}/{zoom}/{lat}/{long}.png?appid={api_key}'.format(map_type=layer,zoom=z,lat=x,long=y,api_key=OWM_API_KEY)
    response = requests.get(url)
    file = open("map.jpg", "wb")
    file.write(response.content)
    file.close()


def main():
    #create and save map image from API
    map_image = get_open_weather_map_layer(OWM_API_KEY,'temp_new','0','0','0')
    
if __name__ =='__main__':
    main()