import tkinter as tk
import requests
from config import API_KEY
from PIL import Image, ImageTk
from io import BytesIO

def get_weather():

    city = city_entry.get()

    if city.strip() == "":
        city_label.config(text = "Please Enter a City Name")
        return
    
    url = url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)

    data = response.json()

    if data["cod"] != 200:
        city_label.config(text = "City Not Found")
        
        temp_label.config(text = "")
        humidity_label.config(text = "")
        wind_label.config(text = "")
        condition_label.config(text = "")
        icon_label.config(image = "")

        return
    
    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    condition = data["weather"][0]["description"]
    icon_code = data["weather"][0]["icon"]

    city_label.config(text = city_name)

    temp_label.config(text = f"Temperature: {temperature} °C")

    humidity_label.config(text = f"Humidity: {humidity}%")

    wind_label.config(text = f"Wind Speed: {wind_speed} m/s")

    condition_label.config(text = f"Condition: {condition}")

    icon_url = (f"https://openweathermap.org/img/wn/{icon_code}@2x.png")

    icon_response = requests.get(icon_url)

    image_data = icon_response.content

    image = Image.open(BytesIO(image_data))

    image = image.resize((120,120))
    weather_icon = ImageTk.PhotoImage(image)
    icon_label.config(image = weather_icon)
    icon_label.image = weather_icon

# -----------------------------------
# GUI Window
# -----------------------------------

root = tk.Tk()

root.title("Weather Application")
root.geometry("500x600")
root.resizable(False, False)

# Heading
heading_label = tk.Label(
    root,
    text = "Weather Application",
    font = ("Calibri", 26, "bold")
)
heading_label.pack(pady=20)

# City Entry
city_entry = tk.Entry(
    root,
    font = ("Arial", 16),
    width = 25
)
city_entry.pack(pady=20)

# Search Button
search_btn = tk.Button(
    root,
    text = "Search",
    font = ("Arial", 16),
    command = get_weather
)
search_btn.pack(pady=10)

# Icon Label
icon_label = tk.Label(root)
icon_label.pack(pady=20)

# City Label
city_label = tk.Label(
    root,
    text = "",
    font = ("Arial", 20, "bold")
)
city_label.pack(pady=10)

# Temperature Label
temp_label = tk.Label(
    root,
    text = "",
    font = ("Arial", 16,)
)
temp_label.pack(pady=5)

# Humidity Label
humidity_label = tk.Label(
    root,
    text = "",
    font = ("Arial", 16)
)
humidity_label.pack()

# Wind Speed Label
wind_label = tk.Label(
    root,
    text = "",
    font = ("Arial", 16)
)
wind_label.pack(pady=5)

# Condition Label
condition_label = tk.Label(
    root,
    text = "",
    font = ("Arial", 16)
)
condition_label.pack(pady=5)

root.mainloop()