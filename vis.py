from influxdb_client import InfluxDBClient
import matplotlib.pyplot as plt

# InfluxDB connection details
url = "http://localhost:8086"
token = "5cyw7teT5nnwsbCUg6OAToq3zdewu4X07AyLxM0HPJWVv6W5jNTfjYT4izvmOOZufZwfjB98_VxIJz7KLuSo5g=="
org = "PPU"
bucket = "temperature_data"

client = InfluxDBClient(url=url, token=token, org=org)

# Query temperature data from InfluxDB
def query_data():
    query = 'from(bucket:"temperature_data") |> range(start: -1h) |> filter(fn: (r) => r._measurement == "temperature")'
    tables = client.query_api().query(query, org=org)
    return tables

# Plot temperature data using Matplotlib
def plot_data(tables):
    times = []
    values = []

    for table in tables:
        for record in table.records:
            times.append(record.values['_time'])
            values.append(record.values['_value'])

    plt.plot(times, values, marker='o', label='Temperature')

    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Temperature Sensor Data')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    tables = query_data()
    plot_data(tables)
