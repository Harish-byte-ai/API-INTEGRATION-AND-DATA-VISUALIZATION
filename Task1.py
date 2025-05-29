import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

# ----------------------------
# CONFIGURATION
# ----------------------------
API_KEY = '9216ff9c97e1e61239be9a234a8c4fbc'  # Replace with your OpenWeatherMap API key
CITY = 'Chennai'
DAYS = 5
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"


# ----------------------------
# FETCH WEATHER DATA
# ----------------------------
def fetch_weather_data():
    response = requests.get(URL)
    data = response.json()
    if 'list' not in data:
        print("Error fetching data:", data.get('message', 'Unknown error'))
        return []  # return empty list to avoid crash
    return data['list']

# ----------------------------
# PROCESS DATA
# ----------------------------
def process_data(raw_data):
    temps = []
    times = []

    for entry in raw_data:
        temp = entry['main']['temp']
        dt_txt = entry['dt_txt']
        dt = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
        temps.append(temp)
        times.append(dt)

    return times, temps

# ----------------------------
# VISUALIZE DATA
# ----------------------------
def visualize_weather(times, temps):
    sns.set(style="darkgrid")

    plt.figure(figsize=(14, 6))
    plt.plot(times, temps, marker='o', color='tab:blue', label='Temperature (°C)')
    plt.title(f'5-Day Weather Forecast for {CITY}', fontsize=16)
    plt.xlabel('Date and Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend()
    plt.grid(True)
    plt.show()

# ----------------------------
# MAIN EXECUTION
# ----------------------------
def main():
    print(f"Fetching weather data for {CITY}...")
    raw_data = fetch_weather_data()
    times, temps = process_data(raw_data)
    visualize_weather(times, temps)

if __name__ == '__main__':
    main()

