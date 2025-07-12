"""
CS50 Final Project – SkyTracker
Uses updated API: https://api.wheretheiss.at/v1/satellites/25544
Includes fallback data and visible planet simulation.
"""
from flask import Flask
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
from flask import Flask, render_template, jsonify
import requests
from datetime import datetime, timedelta
from random import sample

app = Flask(__name__)

ISS_API = "https://api.wheretheiss.at/v1/satellites/25544"


def get_visible_planets():
    """Simulate visible planets randomly."""
    planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]
    return sample(planets, k=3)


def get_iss_passes(lat, lon):
    """
    Simulate ISS pass times using current UTC time.
    Real-time pass predictions are not available via this API.
    """
    try:
        response = requests.get(ISS_API, timeout=10)
        response.raise_for_status()
        now = datetime.utcnow()
        passes = [
            {"risetime": (now).strftime("%Y-%m-%d %H:%M:%S"), "duration": 600},
            {"risetime": (now + timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S"), "duration": 540},
            {"risetime": (now + timedelta(hours=17)).strftime("%Y-%m-%d %H:%M:%S"), "duration": 480},
        ]
        return passes
    except Exception as e:
        print(f"[ERROR] ISS API fallback: {e}")
        return [
            {"risetime": "2025-07-11 20:03:00", "duration": 600},
            {"risetime": "2025-07-12 05:12:00", "duration": 480},
            {"risetime": "2025-07-12 19:50:00", "duration": 540}
        ]


@app.route("/")
def index():
    latitude = -31.9523   # Perth
    longitude = 115.8613
    passes = get_iss_passes(latitude, longitude)
    planets = get_visible_planets()
    return render_template("index.html", passes=passes, planets=planets)


@app.route("/api/iss")
def iss_location():
    try:
        res = requests.get(ISS_API, timeout=10)
        res.raise_for_status()
        data = res.json()
        return jsonify({
            "latitude": data["latitude"],
            "longitude": data["longitude"],
            "altitude": data["altitude"]
        })
    except Exception as e:
        return jsonify({"error": "Failed to fetch ISS location"}), 500


if __name__ == "__main__":
    app.run(debug=True)