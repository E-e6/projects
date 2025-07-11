# 🌌 SkyTracker – ISS Passes Over Perth

#### Video Demo: <PASTE_YOUR_YOUTUBE_LINK_HERE>
#### Author: Eve Modra
#### GitHub: https://github.com/<your-username>
#### edX Username: <your-edx-username>
#### Location: Perth, Australia
#### Date: July 11, 2025

---

## Description:

SkyTracker is a web-based application built with Python and Flask that informs users in Perth, Australia, about the upcoming International Space Station (ISS) passes visible from the city. It also displays a list of planets likely visible in the night sky.

Originally designed to fetch live data from the Open Notify API, the project includes fallback logic with example ISS pass data because the public API was offline during development (confirmed 404 on July 11, 2025). Despite this, the project accurately simulates realistic orbital pass times and integrates dynamic night-sky content.

---

## Features:

- 🌌 Displays next visible ISS pass times over Perth CBD.
- 🪐 Shows three randomly selected planets visible tonight.
- 🌐 Simple, responsive interface with Flask, HTML, and CSS.
- 🔄 Fallback logic for when live API data is unavailable.
- 🔧 Clean modular code with comments and error handling.

---

## Technologies Used:

- Python 3
- Flask
- Requests (HTTP library)
- HTML5 + CSS3 (with Jinja2 templates)
- Open Notify API (fallback simulated)

---

## Files Explained:

- `app.py`: Main Flask server. Handles the `/` route, fetches (or simulates) ISS data, selects planets, and renders `index.html`.
- `templates/index.html`: HTML template rendered using Flask. Uses Jinja2 to insert data like ISS pass times and planet names.
- `static/style.css`: Basic styling for the page layout.
- `requirements.txt`: Python packages used (Flask, Requests).
- `README.md`: This documentation.

---

## Design Decisions:

- The planets shown are selected using Python’s `random.sample()` from a list of 5 commonly visible planets. Future updates could integrate real astronomy APIs (e.g., NASA Horizons or Stellarium).
- Because Open Notify was unavailable, fallback data keeps the app demonstrable. This was done to ensure reliable functionality during demo recording.
- The ISS pass data is shown in local readable format (`YYYY-MM-DD HH:MM:SS`) using `datetime.fromtimestamp()`.

---

## Future Improvements:

- Integrate real-time astronomy APIs for accurate planet visibility.
- Add user geolocation support for worldwide ISS tracking.
- Use Notify/Push notifications for real ISS/planet alerts.
- Build a mobile version or progressive web app (PWA).

---

## Acknowledgements:

- CS50 – Harvard’s Introduction to Computer Science
- Open Notify API – http://api.open-notify.org/
- NASA’s Open Data Resources
