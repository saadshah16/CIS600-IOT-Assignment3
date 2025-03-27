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

📊 ThingSpeak Info
Channel ID: 2894437

Write API Key: 1O2D4JS6LNK1HWYL

Read API Key: LY5T2T12ZEI363PY

Screenshots
Include:

iot_station_simulator.py running (sensor output)
<img width="468" alt="image" src="https://github.com/user-attachments/assets/6820cef8-dc54-436f-acd8-4cd306462851" />


mqtt_to_thingspeak.py running (received + posted)
<img width="468" alt="image" src="https://github.com/user-attachments/assets/c9f7ba7e-b3c3-4b57-8782-6c3615011b00" />


thingspeak_reader.py output
<img width="468" alt="image" src="https://github.com/user-attachments/assets/ac98fb39-1d49-4d30-be93-865417226cbf" />


ThingSpeak graphs live in browser
<img width="468" alt="image" src="https://github.com/user-attachments/assets/f6adb03c-fa80-439e-901d-d6bbaa6228fa" />

🙌 Author
Saad Shah
M.S. Computer Science — Syracuse University

