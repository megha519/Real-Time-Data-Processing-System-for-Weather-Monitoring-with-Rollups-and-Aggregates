# Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates
A real-time weather monitoring system that fetches data from the OpenWeatherMap API every 5 minutes. It computes daily summaries, including average, max, and min temperatures, along with the dominant weather condition. The system also implements alert thresholds for extreme weather and visualizes trends through plots.


## Objective
Develop a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system utilizes data from the [OpenWeatherMap API](https://openweathermap.org/).

## Data Source
The system continuously retrieves weather data from the OpenWeatherMap API. You will need to sign up for a free API key to access the data. The API provides various weather parameters, and we will focus on:
- **main**: Main weather condition (e.g., Rain, Snow, Clear)
- **temp**: Current temperature in Celsius
- **feels_like**: Perceived temperature in Celsius
- **dt**: Time of the data update (Unix timestamp)

## Processing and Analysis
- The system calls the OpenWeatherMap API at configurable intervals (e.g., every 5 minutes) to retrieve real-time weather data for major metros in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad).
- Each received weather update includes:
  - Conversion of temperature values from Kelvin to Celsius (consider user preference).

## Rollups and Aggregates
1. **Daily Weather Summary**:
   - Roll up the weather data for each day.
   - Calculate daily aggregates:
     - Average temperature
     - Maximum temperature
     - Minimum temperature
     - Dominant weather condition (justification required)
   - Store daily summaries in a database or persistent storage for further analysis.

2. **Alerting Thresholds**:
   - Define user-configurable thresholds for temperature or specific weather conditions (e.g., alert if temperature exceeds 35°C for two consecutive updates).
   - Continuously track the latest weather data and compare it with the thresholds.
   - If a threshold is breached, trigger an alert for the current weather conditions (can be displayed on the console or through email notifications).

3. **Implement Visualizations**:
   - Visualize daily weather summaries, historical trends, and triggered alerts.

## Test Cases
1. **System Setup**:
   - Verify the system starts successfully and connects to the OpenWeatherMap API using a valid API key.
   
2. **Data Retrieval**:
   - Simulate API calls at configurable intervals and ensure the system retrieves and parses weather data correctly.
   
3. **Temperature Conversion**:
   - Test conversion of temperature values from Kelvin to Celsius (or Fahrenheit based on user preference).
   
4. **Daily Weather Summary**:
   - Simulate a sequence of weather updates over several days.
   - Verify that daily summaries are calculated correctly, including average, maximum, minimum temperatures, and the dominant weather condition.
   
5. **Alerting Thresholds**:
   - Define and configure user thresholds for temperature or weather conditions.
   - Simulate weather data exceeding thresholds and verify that alerts are triggered only when violations occur.

## Bonus Features
- Support additional weather parameters from the OpenWeatherMap API (e.g., humidity, wind speed) and incorporate them into rollups/aggregates.
- Implement functionalities to retrieve weather forecasts and generate summaries based on predicted conditions.

## Evaluation Criteria
- Functionality and correctness of the real-time data processing system.
- Accuracy of data parsing, temperature conversion, and rollup/aggregate calculations.
- Efficiency of data retrieval and processing within acceptable intervals.
- Completeness of test cases covering various weather scenarios and user configurations.
- Clarity and maintainability of the codebase.
- (Bonus) Implementation of additional features.

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- SQLite
- Requests
- Matplotlib

### Installation
1. **Clone the repository**:
   ```
   git clone https://github.com/your_username/weather_monitoring.git
   cd weather_monitoring
Create a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:


pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory and add your OpenWeatherMap API key:

API_KEY=your_api_key_here
Initialize the database:


python app/database.py
Run the application:



python app/app.py
Usage
Access the application in your browser at http://127.0.0.1:5000/
View the plot of current temperatures by navigating to http://127.0.0.1:5000/plot
License
This project is not licensed.

Acknowledgments
OpenWeatherMap API
vbnet


### Instructions for Use:
- Replace `your_username` in the clone URL with your GitHub username.
- Update the API_KEY section with specific instructions on acquiring and setting up the API key.
- Adjust any details based on your implementation or preferences.

Feel free to modify or expand upon this template as needed! If you have any specific requests or additional sections to include, just let me know.
