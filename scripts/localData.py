#!/usr/bin/env python3
import time, json, logging, requests
from logging.handlers import TimedRotatingFileHandler

# ── CONFIG ──────────────────────────────────────────────────────────────
# Writes log file for Splunk (or w/e) will monitor
LOG_FILE = "/var/log/greenhouse_api.json"
POLL_INTERVAL = 15 * 60    # every 15 minutes

# ── LOGGER SETUP ────────────────────────────────────────────────────────
logger = logging.getLogger("greenhouse_api")
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler(
    LOG_FILE, when="midnight", interval=1, backupCount=7, utc=False
)
handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(handler)

# ── FETCH WTTR.IN DATA ─────────────────────────────────────────────────
def get_external_weather():
    API_KEY = "{YOUR OPENWEATHER MAP API KEY HERE}"

    # Your coordinates
    lat = XX.XXX
    lon = -XX.XXX

    headers = {"User-Agent": "greenhouse-monitor/1.0"}

    # One Call 3.0 endpoint
    url = (
        f"https://api.openweathermap.org/data/3.0/onecall"
        f"?lat={lat}&lon={lon}"
        f"&units=imperial"
        f"&appid={API_KEY}"
    )

    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    current = data["current"]
    daily = data["daily"][0]

    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "weather_temp_f": float(current["temp"]),
        "weather_feelslike_f": int(round(current["feels_like"])),
        "weather_humidity": int(current["humidity"]),
        "weather_cloudcover": int(current["clouds"]),
        "weather_pressure_in": round(current["pressure"] * 0.02953, 2),  # hPa → inches
        "weather_wind_mph": float(current["wind_speed"]),
        "weather_uv_index": int(current.get("uvi", 0)),
        "moon_illumination": int(daily.get("moon_phase", 0) * 100),
        "moon_phase": str(daily.get("moon_phase", 0)),
        "sunrise": time.strftime("%I:%M %p", time.localtime(current["sunrise"])),
        "sunset": time.strftime("%I:%M %p", time.localtime(current["sunset"])),
        "moonrise": time.strftime("%I:%M %p", time.localtime(daily["moonrise"])),
        "moonset": time.strftime("%I:%M %p", time.localtime(daily["moonset"])),
    }

# ── MAIN LOOP ──────────────────────────────────────────────────────────
def api_logger():
    while True:
        try:
            entry = get_external_weather()
        except Exception as e:
            entry = {
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
                "weather_error": str(e)
            }
        logger.info(json.dumps(entry))
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    api_logger()
