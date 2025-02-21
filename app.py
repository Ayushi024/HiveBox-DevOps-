import os
from flask import Flask, jsonify
import requests
from dotenv import load_dotenv

# Load environment variables from .env (for local development)
load_dotenv()

app = Flask(__name__)

# Get API key securely from environment variables
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not OPENWEATHER_API_KEY:
    raise ValueError("⚠️ OPENWEATHER_API_KEY is not set in the environment!")

@app.route("/version", methods=["GET"])
def get_version():
    """Returns the version of the deployed app."""
    return jsonify({"version": "v0.0.1"})

@app.route("/temperature", methods=["GET"])
def get_temperature():
    """Fetches the latest temperature data from OpenWeather API."""
    city = "Delhi"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        return jsonify({"temperature_celsius": temp})
    else:
        return jsonify({"error": "Failed to fetch data", "details": response.text}), response.status_code

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
