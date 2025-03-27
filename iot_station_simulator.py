import paho.mqtt.client as mqtt
import random
import time
import json

MQTT_BROKER = "mqtt.eclipseprojects.io"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/saad_station"

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(-50, 50), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "co2": random.randint(300, 2000),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def publish_sensor_data(interval=15):
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT)

    try:
        while True:
            data = generate_sensor_data()
            payload = json.dumps(data)
            client.publish(MQTT_TOPIC, payload)
            print(f"📡 Published: {data}")
            time.sleep(interval)
    except KeyboardInterrupt:
        client.disconnect()
        print("⛔ Disconnected")

if __name__ == "__main__":
    publish_sensor_data()
