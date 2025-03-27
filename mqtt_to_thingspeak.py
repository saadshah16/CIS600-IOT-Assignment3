import paho.mqtt.client as mqtt
import json
import requests

# ThingSpeak Config
THINGSPEAK_API_KEY = "1O2D4JS6LNK1HWYL"
THINGSPEAK_URL = "https://api.thingspeak.com/update"
MQTT_TOPIC = "iot/saad_station"

def send_to_thingspeak(temp, hum, co2):
    try:
        response = requests.get(
            THINGSPEAK_URL,
            params={
                "api_key": THINGSPEAK_API_KEY,
                "field1": temp,
                "field2": hum,
                "field3": co2
            },
            timeout=5
        )
        print(f"✅ Data sent to ThingSpeak: {response.status_code}")
    except Exception as e:
        print(f"❌ Error sending to ThingSpeak: {e}")

def on_connect(client, userdata, flags, rc):
    print("🔗 Connected to MQTT broker")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"📥 Received: {payload}")
        send_to_thingspeak(payload["temperature"], payload["humidity"], payload["co2"])
    except Exception as e:
        print(f"❌ Error parsing message: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_forever()
