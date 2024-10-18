from flask import Flask, render_template,send_file
import requests
import time
from datetime import datetime
import threading
from database import init_db, insert_weather_data, get_weather_data
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64


API_KEY = '63ad49cb81cab114d4ed1cbaec348c6b'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

ALERT_THRESHOLD = 35  # User-configurable threshold
ALERT_CONSECUTIVE_UPDATES = 2
consecutive_alerts = {city: 0 for city in CITIES}


app = Flask(__name__, template_folder='templates')

# OpenWeatherMap API setup

@app.route('/')
def index():
    weather_data = get_weather_data()
    return render_template('index.html', weather_data=weather_data)



def check_alerts(city, temperature):
    global consecutive_alerts
    if temperature > ALERT_THRESHOLD:
        consecutive_alerts[city] += 1
        if consecutive_alerts[city] >= ALERT_CONSECUTIVE_UPDATES:
            print(f"Alert! {city} has exceeded the temperature threshold of {ALERT_THRESHOLD}°C.")
    else:
        consecutive_alerts[city] = 0  # Reset alert count if below threshold
def fetch_weather():
    while True:
        for city in CITIES:
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                temperature = data['main']['temp']
                feels_like = data['main']['feels_like']
                weather_condition = data['weather'][0]['main']
                insert_weather_data(city, temperature, feels_like, weather_condition)
                if datetime.now().hour ==0:
                    calculate_daily_summary(city)
            else:
                print(f"Failed to retrieve data for {city}: {response.status_code}")

        time.sleep(300)
@app.route('/plot')
def plot():
    weather_data = get_weather_data()
    cities = [data[0] for data in weather_data]  # Index 0 for city
    temperatures = [data[1] for data in weather_data]  # Index 1 for temperature

    plt.figure(figsize=(10, 6))
    plt.bar(cities, temperatures, color='skyblue')
    plt.title('Current Temperature in Different Cities')
    plt.xlabel('Cities')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    
    # Save the plot to a BytesIO object and encode it to a base64 string
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    plot_url = base64.b64encode(img.getvalue()).decode('ascii')

    return render_template('plot.html', plot_url=plot_url)

if __name__ == '__main__':
    init_db()
    fetch_thread = threading.Thread(target=fetch_weather)
    fetch_thread.daemon = True  # This allows the thread to exit when the main program exits
    fetch_thread.start()
    app.run(debug=True)
