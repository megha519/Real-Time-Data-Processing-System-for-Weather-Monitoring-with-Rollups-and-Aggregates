# app/utils.py
import requests
from datetime import datetime
from app.models import WeatherData, db
from flask import current_app
import os

def fetch_weather_data(city):
    api_key = os.getenv('API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return {
        "city": city,
        "main": data["weather"][0]["main"],
        "temp": data["main"]["temp"] - 273.15,  # Convert from Kelvin to Celsius
        "feels_like": data["main"]["feels_like"] - 273.15,
        "date_time": datetime.utcfromtimestamp(data["dt"])
    }

def save_weather_data(data):
    weather = WeatherData(
        city=data["city"],
        main=data["main"],
        temp=data["temp"],
        feels_like=data["feels_like"],
        date_time=data["date_time"]
    )
    db.session.add(weather)
    db.session.commit()
