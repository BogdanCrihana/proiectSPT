import asyncio
import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self):
        self.client = mqtt.Client()
        self.broker_url = "90e53740d0f446b8aef77a5fab1303ac.s2.eu.hivemq.cloud"
        self.broker_port = 8883  # Portul implicit pentru MQTT over TLS
        self.username = "bogdan"  # Specificați numele de utilizator aici
        self.password = "Unitbv2023"  # Specificați parola aici
        self.loop = asyncio.get_event_loop()
        self.sensor_data = {}

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Conectat la broker MQTT")
        else:
            print(f"Eroare la conectarea la broker MQTT, codul: {rc}")

    def on_message(self, client, userdata, message):
        topic = message.topic
        payload = message.payload.decode()
        self.sensor_data[topic] = payload

    async def connect(self):
        self.client.username_pw_set(self.username, self.password)
        self.client.tls_set()
        self.client.connect_async(self.broker_url, self.broker_port)
        self.client.loop_start()

    async def get_sensor_data(self, sensor_id: str):
        topic = f"sensor/{sensor_id}"
        self.client.subscribe(topic)
        self.client.publish(topic, "get_data")

        while topic not in self.sensor_data:
            await asyncio.sleep(1)

        return self.sensor_data.pop(topic)
