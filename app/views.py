import sqlite3
from flask import jsonify
from app import app  # Ensure this imports your Flask app

@app.route('/')
def home():
    return "Welcome to the Weather Monitoring App!"

@app.route('/fetch', methods=['POST'])
def fetch_weather():
    # Your existing fetch_weather logic
    pass  # Replace with your actual logic

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    # Your existing get_weather logic
    pass  # Replace with your actual logic


@app.route('/daily_summary', methods=['GET'])
def get_daily_summary():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM daily_summary ORDER BY date DESC')
    summaries = cursor.fetchall()
    conn.close()
    return jsonify(summaries)  # This will allow you to fetch the summary data in JSON format for visualization.
