from datetime import datetime
import sqlite3

def init_db():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            feels_like REAL,
            weather_condition TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            date DATE,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_daily_summary(city, avg_temp, max_temp, min_temp, dominant_condition):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO daily_summary (city, date, avg_temp, max_temp, min_temp, dominant_condition)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (city, datetime.now().date(), avg_temp, max_temp, min_temp, dominant_condition))
    conn.commit()
    conn.close()

def calculate_daily_summary(city):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 
            AVG(temperature) as avg_temp, 
            MAX(temperature) as max_temp, 
            MIN(temperature) as min_temp,
            weather_condition
        FROM weather 
        WHERE city = ? AND DATE(timestamp) = DATE('now')
        GROUP BY weather_condition
    ''', (city,))
    data = cursor.fetchall()
    if data:
        avg_temp = data[0][0]
        max_temp = data[0][1]
        min_temp = data[0][2]
        dominant_condition = data[0][3]
        insert_daily_summary(city, avg_temp, max_temp, min_temp, dominant_condition)
    conn.close()

def insert_weather_data(city, temperature, feels_like, weather_condition):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    # Check for existing records within the last 5 minutes
    cursor.execute('''
        SELECT id, temperature, feels_like, weather_condition FROM weather 
        WHERE city = ? AND timestamp >= datetime('now', '-5 minutes')
    ''', (city,))
    existing_record = cursor.fetchone()

    if existing_record:
        # If a record exists, compare it to the new data
        existing_temp, existing_feels_like, existing_condition = existing_record[1], existing_record[2], existing_record[3]
        
        # Check if the new data is different enough to warrant an update
        if (temperature != existing_temp or 
            feels_like != existing_feels_like or 
            weather_condition != existing_condition):
            cursor.execute('''
                UPDATE weather
                SET temperature = ?, feels_like = ?, weather_condition = ?, timestamp = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (temperature, feels_like, weather_condition, existing_record[0]))
            print(f"Updated data for {city}.")
        else:
            print(f"Data for {city} is the same as the existing record. Skipping insert.")
    else:
        # Insert new record
        cursor.execute('''
            INSERT INTO weather (city, temperature, feels_like, weather_condition)
            VALUES (?, ?, ?, ?)
        ''', (city, temperature, feels_like, weather_condition))
        print(f"Inserted new data for {city}.")

    conn.commit()
    conn.close()

def get_weather_data():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('SELECT city, temperature, feels_like, weather_condition, timestamp FROM weather ORDER BY timestamp DESC')
    data = cursor.fetchall()
    conn.close()
    return data
