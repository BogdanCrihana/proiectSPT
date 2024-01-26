import paho.mqtt.client as mqtt
import time
import random

broker_url = "broker.hivemq.com"
sensor_ids = ["temperature", "humidity", "pressure"]

def simulate_sensors():
    client = mqtt.Client()
    client.connect(broker_url)
    
    while True:
        for sensor_id in sensor_ids:
            sensor_value = round(random.uniform(0, 100), 2)
            client.publish(f"sensor/{sensor_id}", str(sensor_value))
        time.sleep(5)

if __name__ == "__main__":
    simulate_sensors()
