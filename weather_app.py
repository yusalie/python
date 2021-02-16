# Import libraries
import requests
from tkinter import *
from datetime import *

# Creates tkinter window
window = Tk()

# Creates widgets
dte_tme = Label(window, text="Date/time")
temp_label = Label(window, text="temperature")
feel_lb = Label(window, text="feels like")
max_lb = Label(window, text="max temp")
min_lb = Label(window, text="min temp")
locat_input = Entry(window)
humid_lb = Label(window, text="Humidity")
cloud_lb = Label(window, text="Cloud cover")
wind_lb = Label(window, text="wind speed")

# Creates function
def update_temp():
    # Gets request from api
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+locat_input.get()+'&appid=9cef29be427e4cf75cd3ac86c23ce222')
    # fetches json data from url
    rj = r.json()
    # fetches temperature from json
    temp = rj['main']['temp']
    
    # converts temperture in json and rounds it to two decimals
    temp_con = round(temp - 273, 2)
    feel_ = rj['main']['feels_like']
    feel_con = round(feel_ - 273, 2)
    max_ = rj['main']['temp_max']
    max_con = round(max_ - 273, 2)
    min_ = feel_ = rj['main']['temp_min']
    min_con = round(min_ - 273, 2)
    
    # Updates label with json data
    temp_label.config(text="The temperature is: "+str(temp_con))
    feel_lb.config(text="Feels like: " + str(feel_con))
    max_lb.config(text="Max temp is: " + str(max_con))
    min_lb.config(text="Min temp is: " + str(min_con))
    wind_lb.config(text="wind speed: " + str(rj['wind']['speed'])+ "km/h")
    cloud_lb.config(text="Cloud cover: " + str(rj['weather'][0]['description']))
    humid_lb.config(text="Humidity: " + str(rj['main']['humidity']))
    
    # Gets current time from a specific place
    time_z = int(rj['timezone'] /3600)
    delta_z = time_z -2
    dt_now = datetime.now()
    time_cur = dt_now.strftime("%H,%M")
    nt = dt_now + timedelta(hours=delta_z)
    nt = nt.strftime("%H:%M")
    dte_tme.config(text="time in " +locat_input.get()+": " + nt)
      
    
      

# Button that uses the function
upd_btn = Button(window, text="update weather", command=update_temp)


locat_input.grid()
temp_label.grid()
feel_lb.grid()
max_lb.grid()
min_lb.grid()
wind_lb.grid()
cloud_lb.grid()
dte_tme.grid()
upd_btn.grid()
window.mainloop()