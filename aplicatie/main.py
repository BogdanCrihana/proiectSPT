from fastapi import FastAPI
from mqtt_client import MQTTClient
import asyncio

app = FastAPI()
mqtt_client = MQTTClient()

@app.get("/sensor-data/{sensor_id}")
async def read_sensor_data(sensor_id: str):
    data = await mqtt_client.get_sensor_data(sensor_id)
    return {"sensor_id": sensor_id, "data": data}

async def main():
    loop = asyncio.get_event_loop()
    loop.create_task(mqtt_client.connect())
    await asyncio.sleep(0)    

if __name__ == "__main__":
    asyncio.run(main())
    uvicorn.run(app, host="0.0.0.0", port=8883)
