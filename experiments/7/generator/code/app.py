import time
from datetime import datetime
from influxdb import InfluxDBClient


def add_to_influx(val):

    json_body = [
        {
            "measurement": "some_measurement",
            "tags": {"sample_tag": "sample_tag_value"},
            "time": datetime.now(),
            "fields": {"value": val},
        }
    ]

    client = InfluxDBClient("influxdb", 8086, "admin", "admin", "db0")
    client.write_points(json_body)

    print("Added {}".format(val))


def generate_curve():

    x = 100.0

    while x > 1:
        time.sleep(1)
        add_to_influx(x)
        x = x * 0.99


if __name__ == "__main__":

    generate_curve()
    print("Finished")
