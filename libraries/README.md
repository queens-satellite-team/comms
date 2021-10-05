# GUI Builder 🛠️
1.0 Run the `gui_builder.py` file as the main program to see an example GUI. Example: `python3 gui_builder.py`

2.0 Import the gui_builder library in your own file to have access to all the available methods. `import library.gui_builder as build`

2.1 Example use: `app = build.init_app("WEATHER GUI")`

# Weather 🌤️
1.0 Run the `weather.py` file as the main program to see an example use. Example: `python3 gui_builder.py`

2.0 Import the weather library in your own file to have access to all the available methods. `import library.weather as weather`

2.1 Example use: `weather_dict = weather.get_gov_weather_by_station(station_id)`

## Open Weather Map Setup 
To use some features of the weather library, an acount must be created in order to access the free public API. 

1.0 Register for an acount at [Open Weather Map](https://openweathermap.org/) and generate your individul API key. 

2.0 Create a file called API_KEY.py and insert the line `OWM_API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'` where the x's are your API key. 

2.1 Place this file into the same library directory as `weather.py`. You now have access to the open weather map functions.  
