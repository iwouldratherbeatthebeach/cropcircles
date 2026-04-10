# 🌱 Greenhouse Operations Dashboard

A Splunk-powered greenhouse monitoring and observability platform for tracking environmental conditions, outdoor weather, plant-specific growing ranges, and alert conditions in real time.

This project combines greenhouse sensor scripts with a Splunk dashboard to provide operational visibility into temperature, humidity, VPD (vapor pressure deficit), dew point, outdoor comparison, plant compatibility, and environmental alarms.

Designed for both manual greenhouse management and future automation workflows.

---

## 📊 Features

### Real-Time Monitoring

- Greenhouse temperature tracking
- Humidity tracking
- Dew point calculation
- Vapor Pressure Deficit (VPD)
- Dew point spread (condensation risk indicator)
- Sensor freshness monitoring

### Environmental Intelligence

- Greenhouse vs outdoor temperature comparison
- Greenhouse vs outdoor humidity comparison
- Temperature delta vs outdoor
- Humidity delta vs outdoor
- 24-hour stability score
- Hour-of-day environmental averages

### Plant-Aware Logic

Supports environmental targets for:

- Coffee
- Green tea
- Jasmine
- Cavendish banana
- Pink Lemonade blueberry
- Kale
- Tobacco
- Peppers
- Corn
- Black pepper
- Dahlias
- Flowers

Each plant includes:

- Recommended temperature range
- Recommended humidity range
- Recommended VPD range
- Live compatibility status

---

## 🚨 Alerts

Built-in alarms include:

| Condition | Trigger |
|----------|---------|
| Low temperature | Below 45°F |
| High temperature | Above 95°F |
| Low humidity | Below 35% |
| High humidity | Above 90% |
| Condensation risk | Dew point spread collapse |

Plant-specific environmental range checks are also included.

---

## 🧠 Dashboard Sections

### KPI Panels

- Greenhouse temperature
- Humidity
- VPD
- Dew point
- Sensor age
- Temperature delta vs outdoor

### Alarm Panels

- Temperature alarm
- Humidity alarm
- Dew point spread warning

### Trend Panels

- Temperature trend
- Humidity trend
- VPD trend
- Dew point trend
- Daily temperature high / low / average
- Hourly environmental averages

### Outdoor Weather Snapshot

Includes:

- Outdoor temperature
- Feels-like temperature
- Outdoor humidity
- Wind
- UV index
- Pressure
- Sunrise / sunset
- Moonrise / moonset
- Moon illumination

### Plant Intelligence Panels

- Plants currently inside VPD range
- Plants currently inside temperature/humidity range
- Plant environment reference vs live conditions
- Plant VPD reference vs live conditions

### Operational Health Panels

- Recent alert events
- Alert count by day
- Data source freshness

---

## 📡 Data Sources

### Greenhouse Sensor Logs

Search:

    index=greenhouse sourcetype="greenhouse:log"

Expected format example:

    - 78.2°F 61.0%

Used for:

- temperature
- humidity
- dew point
- VPD
- alerts
- plant compatibility scoring

### Weather API JSON Input

Search:

    index=greenhouse sourcetype="greenhouse:api:json"

Used for:

- outdoor temperature
- humidity
- wind
- UV index
- pressure
- cloud cover
- sunrise / sunset
- moonrise / moonset
- moon illumination

---

## 📐 Calculated Metrics

### Vapor Pressure Deficit (VPD)

Derived from greenhouse temperature and humidity to estimate plant transpiration stress.

### Dew Point

Used to estimate condensation and mold risk.

### Dew Point Spread

Difference between greenhouse temperature and dew point. Smaller spread increases condensation probability.

### Stability Score

Rolling score calculated from temperature and humidity variation over the last 24 hours.

Output range:

    0 – 100

Higher is better.

---

## 🌿 Plant Environment Reference

| Plant | Temp | Humidity | VPD |
|------|------|----------|-----|
| Coffee | 60–75°F | 50–70% | 0.8–1.2 |
| Green Tea | 55–75°F | 40–70% | 0.6–1.0 |
| Jasmine | 60–80°F | 50–70% | 0.8–1.2 |
| Cavendish Banana | 70–95°F | 60–90% | 0.9–1.5 |
| Pink Lemonade Blueberry | 45–80°F | 40–65% | 0.6–1.1 |
| Kale | 45–75°F | 40–70% | 0.7–1.0 |
| Tobacco | 65–85°F | 50–75% | 0.9–1.2 |
| Peppers | 65–85°F | 50–75% | 0.8–1.2 |
| Corn | 60–95°F | 40–70% | 0.8–1.3 |
| Black Pepper | 70–90°F | 60–85% | 0.6–0.9 |
| Dahlias | 60–80°F | 50–70% | 0.8–1.2 |
| Flowers | 55–80°F | 45–70% | 0.8–1.2 |

---

## 🏗 Architecture

    Sensors
        ↓
    Logger Scripts
        ↓
    Splunk Ingestion
        ↓
    Greenhouse Index
        ↓
    Dashboard Visualization
        ↓
    Alert Logic
        ↓
    Future Automation

Future automation targets include:

- irrigation
- ventilation
- fans
- misting systems
- pumps
- solenoids
- relays

---

## 📁 Repository Structure Example

    greenhouse-ops/
    ├── README.md
    ├── dashboard/
    │   └── greenhouse_operations_dashboard.xml
    ├── scripts/
    │   ├── greenhouse_logger.py
    │   ├── weather_poll.py
    │   ├── sensor_read.py
    │   ├── alerting.py
    │   ├── irrigation_control.py
    │   └── fan_control.py
    ├── configs/
    │   ├── inputs.conf
    │   ├── props.conf
    │   └── transforms.conf
    └── docs/
        └── architecture.md

---

## 🚀 Dashboard Installation

Place the dashboard XML inside:

    $SPLUNK_HOME/etc/apps/<your_app>/local/data/ui/views/

Restart Splunk or reload the UI.

Confirm access to:

    index=greenhouse sourcetype="greenhouse:log"
    index=greenhouse sourcetype="greenhouse:api:json"

---

## 🔧 Scripts

Scripts support the telemetry pipeline behind the dashboard.

Typical responsibilities include:

- sensor polling
- environmental logging
- weather API enrichment
- Splunk forwarding
- alert generation
- irrigation triggers
- ventilation triggers
- relay control

Compatible platforms include:

- Raspberry Pi
- ESP32
- Arduino
- Linux servers

---

## 🧭 Roadmap

Planned improvements:

- plant selector tokens
- plant-aware alarm thresholds
- forecast integration
- irrigation automation
- ventilation automation
- Cloudflare public dashboard mode
- mobile dashboard layout
- anomaly detection scoring
- relay orchestration layer

---

## 📜 License

GNU 3.0
