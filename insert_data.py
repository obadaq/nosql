from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime
import random
import time

# InfluxDB connection details
url = "http://localhost:8086"
token = "5cyw7teT5nnwsbCUg6OAToq3zdewu4X07AyLxM0HPJWVv6W5jNTfjYT4izvmOOZufZwfjB98_VxIJz7KLuSo5g=="
org = "PPU"
bucket = "temperature_data"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Simulate temperature data
def generate_temperature_data():
    return random.uniform(20.0, 30.0)

# Upload simulated data to InfluxDB
def upload_data():
    while True:
        temperature = generate_temperature_data()

        point = Point("temperature").tag("sensor", "sensor_1").field("value", temperature).time(datetime.utcnow())

        write_api.write(bucket=bucket, record=point)
        print(f"Uploaded temperature: {temperature}")
        time.sleep(5)

if __name__ == "__main__":
    upload_data()
