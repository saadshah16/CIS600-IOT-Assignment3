# 🌐 IoT Weather Station — CIS600 Assignment 3

This project simulates an IoT environment station that generates temperature, humidity, and CO₂ data and publishes it to a cloud service (ThingSpeak) via MQTT and REST API. It includes a live data simulator, a cloud bridge, and a CLI-based data viewer.

---

## 📂 Project Structure

| File | Description |
|------|-------------|
| `iot_station_simulator.py` | Publishes simulated sensor data via MQTT every 15 seconds |
| `mqtt_to_thingspeak.py` | Subscribes to MQTT and pushes data to ThingSpeak |
| `thingspeak_reader.py` | Fetches latest or historical data and displays chart |


---

## ⚙️ How It Works

1. `iot_station_simulator.py` generates fake sensor data every 15 seconds and publishes it to the topic:  
   **`iot/saad_station`** via the public broker `mqtt.eclipseprojects.io`.

2. `mqtt_to_thingspeak.py` subscribes to the same MQTT topic, receives the data, and posts it to [ThingSpeak](https://thingspeak.com) using your **Write API Key**.

3. `thingspeak_reader.py` can fetch:
   - The **latest sensor values**, or
   - Plot the **last 5 hours** of any one sensor (temperature/humidity/co2) using the ThingSpeak **Read API Key**.

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/CIS600-IoT-Assignment3.git
cd CIS600-IoT-Assignment3

### 2. Install dependencies
pip install -r requirements.txt


### 3. Start Sensor Publisher(Terminal 1)
python iot_station_simulator.py


### 4. Start MQTT → ThingSpeak Bridge (Terminal 2)
python mqtt_to_thingspeak.py


### 5. View or Plot Data (Terminal 3)
python thingspeak_reader.py

