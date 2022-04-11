import tkinter as tk
from tkinter import Label, Menu, PhotoImage, StringVar
from tkinter import ttk
from tkinter import scrolledtext
from tkintermapview import TkinterMapView
from tkinter import messagebox
from API_KEY import OWM_API_KEY
import PIL.Image as pii
import PIL.ImageTk as pit



def init_app(name):
    """
        breif: Adds a title, sets window sizes, and creates menubar for a root application. 
        return: the instance of the application. 
    """
    root = tk.Tk()
    root.title(f'{name}')
    root.minsize(width=512, height=264) 
    generate_menubar(root)
    return root

def quit_app(root):
    """
        breif: call back for quiting the application 
        return: None
    """
    root.quit()
    root.destroy()
    exit()

def generate_menubar(root):
    """
        breif: creates a menu bar for general saving, opening, closing functions 
        return: None 

        param: root - the main application that is running 
    """
    menu_bar = Menu()
    root.config(menu=menu_bar)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label='New')
    file_menu.add_separator()
    file_menu.add_command(label='Open')
    file_menu.add_separator()
    file_menu.add_command(label='Save')
    menu_bar.add_cascade(label='File', menu=file_menu)

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label='About')
    menu_bar.add_cascade(label='Help', menu=help_menu)

    quit_menu = Menu(menu_bar, tearoff=0)
    quit_menu.add_command(label='Close', command=lambda:quit_app(root))
    menu_bar.add_cascade(label='Exit', menu=quit_menu) 

def create_tab_control(root):
    """
        brief: create a tab controller to house multiple tabs in the GUI
        return: the tkinter notebook tab control 

        param: root - the main application that is running 
    """
    return ttk.Notebook(root)

def create_tab(tab_control, name:str='Tab'):
    """
        breif: adds a tab to the app interface
        return: tab         - the generated tk tab

        param: tab_control  - the controller for all tabs
        param: name         - the name given to the tab
    """
    tab = ttk.Frame(tab_control)           # create
    tab_control.add(tab, text=f'{name}')     # add
    tab_control.pack(expand=1, fill='both') # display
    return tab

def create_frame(tab, r:int=0, c:int=0, name:str='Window'):
    """
        breif: adds a frame to a tab
        return: frame   - the generated frame

        param: tab      - the tab to which to add the frame
        param: r        - the row of the tab
        param: c        - the column of the tab
        param: name     - the name given to the frame
    """
    frame = ttk.LabelFrame(tab, text=f'{name}: ')
    frame.grid(row=r, column=c, padx=8, pady=4, sticky='W')
    return frame

def create_scroll_box(frame, r:int=0, c:int=0, s:int=3, w:int=32, h:int=24):
    """
        breif: generates a text box with a scollbar
        return: frame   - the generated scroll box

        param: frame    - the frame to which to add the scroll box
        param: r        - the row of the tab
        param: c        - the column of the tab
        param: s        - the column span of the scroll box
        param: w        - the width in ASCII units? of the scroll box
        param: h        - the height in ASCII units? of the scroll box
    """
    scr = scrolledtext.ScrolledText(frame, width=w, height=h, wrap=tk.WORD)
    scr.grid(row=r, column=c, columnspan=s, sticky='W')
    return scr

def create_label(frame, r:int=0, c:int=0, s:int=0):
    """
        breif: generates a label that can exist within a tk frame 
        return: frame   - the generated label

        param: frame    - the frame to which to add the scroll box
        param: r        - the row of the tab
        param: c        - the column of the tab
        param: s        - the column span of the scroll box
    """
    temp_label = tk.StringVar()
    ttk.Label(frame, textvariable=temp_label).grid(row=r, column=c, columnspan=s, sticky='W')
    return temp_label

def create_label_and_entry(frame, r:int=0, c:int=0, size:int=16, name:str='Entry'):
    """
        breif: adds a labelled and a read only entry box to a frame
        return: update  - tk string variable used to set/get the entry box

        param: frame    - the frame to which to add the label and entry 
        param: r        - the row of the frame
        param: c        - the column of the frame
        param: name     - the name given to the label
    """
    ttk.Label(frame, text=f'{name}: ').grid(row=r, column=c, padx=8, pady=4, sticky='W')
    update = tk.StringVar()
    updateEntry = ttk.Entry(frame, width=size, textvariable=update, state='readonly')
    updateEntry.grid(row=r, column=c+1, sticky='W')
    return update

def create_label_and_combo(frame, entries, r:int=0, c:int=0, name:str='Combo'):
    """
        breif:              - adds a labelled dropdown box to a specified frame
        return: combo_str   - the tk string variable. What is highlighted in the combo box can be used to set/get with this return variable. 

        param: frame    - the frame to which to add the dropdown box
        param: entries  - a list of all the entries to apear in the dropdown box
        param: r        - the row of the frame
        param: c        - the column of the frame
        param: name     - the name given to the label
    """
    ttk.Label(frame, text=f'{name}').grid(row=r, column=c, padx=8, pady=4, sticky='W')

    combo_str = tk.StringVar()
    strSelected = ttk.Combobox(frame, width=16, textvariable=combo_str)
    strSelected['values'] = entries
    strSelected.grid(column=1, row=0, padx=8, pady=4, sticky='W')
    strSelected.current(0)
    max_width = max([len(x) for x in strSelected['values']])
    strSelected.config(width=max_width+1)
    return combo_str

def create_label_and_button(frame, cmd, r:int=0, c:int=0, name:str='Button'):
    """
        breif: generates a labelled button. Label apears on the button.
        return: the button instance. 

        param: frame    - the tk frame that holds the labelled button
        param: cmd      - lamda function that gets called with a button press. Ex: cmd = lambda: get_station_ids(state_combo_box)
        param: r        - the row of the frame
        param: c        - the column of the frame
        param: name     - the name given to the labelled button
    """
    return ttk.Button(frame, text=f'{name}', command=cmd).grid(row=r, column=c, sticky='W')
        

def entry_at_frame(frame, r:int=0,c:int=0, size:int=16):
    """
        breif: adds an text entry box to a given frame
        return: the entry object

        param: frame    - the frame to which to add the entry box
        param: r        - the row of the frame
        param: c        - the column of the frame
        param: name     - the name given to the label
    """
    entry = tk.Entry(frame)
    entry.pack()
    return entry


def get_coord_entry(entry1, entry2):
    """
        breif: retrieves the conents of latitude and longitiude entry boxes and
                prints their contents to the python console.
        return: the list of coordiniates [lat,long] as a tkinter stringVar

        param: entry1: the latitude entry box content
        param: entry2: the longitude entry box content
    """
    
    lat = entry1.get()
    long = entry2.get()
    
    if (len(lat) != 0 and len(long) != 0):
        try:
            long = float(long)
            lat = float(lat)
            if (float(lat) > 90 or float(lat) < -90) or (float(long) > 180 or float(long) < -180):
                raise Exception ("Range -90 to 90 for latitude and -180 to 180 for longitude")
        except ValueError:
            return "Coordinates must be decimal values."
        
        return [lat,long]
        
    else:
        return ["No Lat.", "No Long."]
    
def create_coord_label(frame, r:int=0, c:int=0, size:int=16, name:str='Entry',value: str=''):
    """
        breif: adds a labelled and a read only entry box to a frame
        return: update  - tk string variable used to set/get the entry box

        param: frame    - the frame to which to add the label and entry 
        param: r        - the row of the frame
        param: c        - the column of the frame
        param: name     - the name given to the label
        param: value    - the string contents of the update string variable
    """
    ttk.Label(frame, text=f'{name}: ').grid(row=r, column=c, padx=8, pady=4, sticky='W')
    update = tk.StringVar()
    update.set(value)
    updateEntry = ttk.Entry(frame, width=size, textvariable=update, state='readonly')
    #updateEntry.pack()
    return update
    

def get_map_type(radio_string_var):
    '''
    breif: using tkinter string variables, returns value of user input
    param: radio_string_var - the tkinter string variable to be returned.
    return: user input for tkinter widget

    
    '''
    print(radio_string_var.get())
    return radio_string_var.get()
    


def main():

    # create the app
    app = init_app("BASIC GUI")

    radio_string_var = tk.StringVar()

    # put a tab controller into the app 
    tab_control =  create_tab_control(app) 

    # create the first tab (ARO) and put it into the controller 
    ARO_tab = create_tab(tab_control, "ARO")

    # create the second tab (MCC)
    MCC_tab = create_tab(tab_control, "MCC")

    #create tab for weather overlays (temp)
    MAP_tab = create_tab(tab_control, "MAP")

    #create tab for interactive map
    interactive_map_tab = create_tab(tab_control, "INT-MAP")
   
    #create a coordinate button frame for ARO coordinate input
    coord_button_frame = create_frame(ARO_tab,0,3,"Enter Coordinates")

    lat_frame = create_frame(ARO_tab, 0, 1, "Enter Latitude")
    long_frame = create_frame(ARO_tab,0,2,"Enter Longtitude")

    #create coordinate entry frames for latitude
    lat_entry = entry_at_frame(lat_frame, 0, 2)

    #create coordinate entry frames for longitude
    long_entry = entry_at_frame(long_frame,0,4)

    # create second button in frame for searching specific location based on coordinates
    coord_enter = create_label_and_button(coord_button_frame, lambda: get_coord_entry(lat_entry, long_entry),0,0,'Enter Coordinates')

    #create lat and long coordinate recieving frames for MCC tab
    lat_display_frame = create_frame(MCC_tab,0,0, "ARO Latitude:")
    long_display_frame = create_frame(MCC_tab,0,1,"ARO Longitude:")

    #place read-only entry box at respective frames for MCC tab
    display_lat = create_coord_label(lat_display_frame,0,0,12,'Lat','{0}'.format(get_coord_entry(lat_entry, long_entry))[0])
    display_long = create_coord_label(long_display_frame,0,0,12,'Long')

    
    #create selection frame in MCC for map type
    select_map_frame = create_frame(ARO_tab,1,1,"Select Map Type")
    map_types=["Clouds","Precipitation","Pressure","Wind Speed","Temperature"]
    #select_map = create_radio_buttons(select_map_frame)
    ttk.Radiobutton(select_map_frame,text="Clouds",variable=radio_string_var,value="clouds_new").pack()
    ttk.Radiobutton(select_map_frame,text="Precipitation",variable=radio_string_var,value="precipitation_new").pack()
    ttk.Radiobutton(select_map_frame,text="Pressure",variable=radio_string_var,value="pressure_new").pack()
    ttk.Radiobutton(select_map_frame,text="Wind Speed",variable=radio_string_var,value="wind_new").pack()
    ttk.Radiobutton(select_map_frame,text="Temperature",variable=radio_string_var,value="temp_new").pack()
    ttk.Button(select_map_frame,text="Submit", command=get_map_type(radio_string_var)).pack()

    #create map overlay
    #create display for map in mcc
    img = pit.PhotoImage(pii.open("map.jpg"),200)
    panel = Label(MAP_tab, image = img)
    panel.grid(column=0, row=0, padx=0, pady=0, sticky='S')
    


    # create interactive map widget
    map_widget = TkinterMapView(interactive_map_tab, width=500, height=500, corner_radius=0) #uses TKinterMapView library by TomSchimansky (github)
    map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    zoom = 0
    x = 0
    y = 0
    layer = 'clouds_new'

    map_widget.set_position(0,0) #enter coords here
    map_widget.set_zoom(0)
    #weather_overlay = wp.get_open_weather_map_layer(OWM_API_KEY,'temp_new',zoom,x,y)
    url = 'https://tile.openweathermap.org/map/{map_type}/{zoom}/{lat}/{long}.png?appid={api_key}'.format(map_type=layer,zoom=zoom,lat=x,long=y,api_key=OWM_API_KEY) 
    #map_widget.set_address("new york city, united states")
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  #create google satellite overlay to interactive map here
    
    #map_widget.set_overlay_tile_server(url)

    
    
    app.mainloop()


if __name__ == '__main__':
    main()
