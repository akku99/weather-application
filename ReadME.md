# Weather Application

A GUI-based Weather Application built using Python, Tkinter, and OpenWeatherMap API that provides real-time weather information for any city.

## Features

* Real-time weather data retrieval
* City search functionality
* Dynamic weather icons
* Temperature display in Celsius
* Humidity monitoring
* Wind speed tracking
* Error handling for invalid city names
* User-friendly Tkinter interface

## Technologies Used

* Python
* Tkinter
* Requests
* Pillow (PIL)
* REST APIs
* JSON

## Project Structure

```text
Weather-App/
│
├── app.py
├── config.py
├── requirements.txt
├── screenshots/
│   ├── home_screen.png
│   ├── weather_result.png
│   └── invalid_city.png
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a config.py file

```python
API_KEY = "YOUR_OPENWEATHER_API_KEY"
```

4. Run the application

```bash
python app.py
```

## Screenshots

### Application Home Screen

![Home Screen](screenshots/home_screen.png)

### Weather Search Result

![Weather Result](screenshots/weather_result.png)

### Invalid City Handling

![Invalid City](screenshots/invalid_city.png)

## Future Enhancements

* 5-day weather forecast
* Search history
* Dark mode support
* Multiple city comparison
* Weather charts and analytics

## Author

Akash Kumar
