"""
CS50 Final Project – SkyTracker
Note: Open Notify API is currently down (confirmed 404 on 2025-07-11).
This project includes fallback ISS data for demonstration purposes.
"""

from flask import Flask, render_template
import requests
from datetime import datetime
from random import sample

app = Flask(__name__)

def get_visible_planets():
    planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]
    return sample(planets, k=3)

@app.route("/")
def index():
    latitude = -31.9523
    longitude = 115.8613
    url = "http://api.open-notify.org/iss-pass.json"
    params = {"lat": latitude, "lon": longitude}

    passes = []
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        for p in data.get("response", []):
            risetime = datetime.fromtimestamp(p["risetime"]).strftime("%Y-%m-%d %H:%M:%S")
            duration = p["duration"]
            passes.append({"risetime": risetime, "duration": duration})
    except Exception as e:
        print(f"Error fetching ISS data: {e}")
        # Use fallback example data
        passes = [
            {"risetime": "2025-07-11 20:03:00", "duration": 600},
            {"risetime": "2025-07-12 05:12:00", "duration": 480},
            {"risetime": "2025-07-12 19:50:00", "duration": 540}
        ]

    visible_planets = get_visible_planets()
    return render_template("index.html", passes=passes, planets=visible_planets)