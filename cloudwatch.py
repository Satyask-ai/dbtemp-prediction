import boto3
import pandas as pd
import numpy as np
import time
import os

# Configuration
AWS_REGION = "us-east-2"  # my aws region is us-east-2
METRIC_NAMESPACE = "DatabaseMonitoring"
METRIC_NAME = "DatabaseTemperature"
CSV_PATH = os.path.join("data", "db_temperature.csv")

# Initialize CloudWatch client
cloudwatch = boto3.client("cloudwatch", region_name=AWS_REGION)

def load_and_simulate_temperature():
    """Loads temperature data, simulates database load, and returns the latest temperature."""
    df = pd.read_csv(CSV_PATH, parse_dates=["Timestamp"])
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df = df.set_index("Timestamp")

    # Simulate database load - add some random fluctuations
    df["temp"] = df["CPU Temperature (°C)"] + np.random.normal(0, 2, len(df))  # Add noise
    df["temp"] = df["temp"].clip(lower=40, upper=90) # Keep temperature within realistic bounds

    latest_temperature = df["temp"].iloc[-1]
    return latest_temperature

def put_metric_data(temperature):
    """Pushes the temperature data to CloudWatch."""
    cloudwatch.put_metric_data(
        Namespace=METRIC_NAMESPACE,
        MetricData=[
            {
                "MetricName": METRIC_NAME,
                "Dimensions": [
                    {
                        "Name": "InstanceId",  
                        "Value": "simulated-db-1" 
                    },
                ],
                "Timestamp": time.time(),  # Current timestamp
                "Value": temperature,
                "Unit": "None",
            },
        ],
    )
    print(f"Sent temperature {temperature}°C to CloudWatch.")

if __name__ == "__main__":
    while True:
        temperature = load_and_simulate_temperature()
        put_metric_data(temperature)
        time.sleep(60)  # Send data every 60 seconds