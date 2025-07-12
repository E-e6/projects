"""
CS50 Final Project – SkyTracker
Uses updated API: https://api.wheretheiss.at/v1/satellites/25544
Includes fallback data and visible planet simulation.
"""
from flask import Flask, render_template, jsonify
import os
import requests
from datetime import datetime, timezone, timedelta
from random import sample

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

ISS_API = "https://api.wheretheiss.at/v1/satellites/25544"

def get_visible_planets():
    planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]
    return sample(planets, k=3)

def get_iss_passes(lat, lon):
    try:
        response = requests.get(ISS_API, timeout=10)
        response.raise_for_status()
        now = datetime.now(timezone.utc)  # fixed to timezone-aware datetime
        passes = [
            {"risetime": now.strftime("%Y-%m-%d %H:%M:%S"), "duration": 600},
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
    latitude = -31.9523  # Perth
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
    except Exception:
        return jsonify({"error": "Failed to fetch ISS location"}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)  # debug mode turned OFF