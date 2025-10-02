import boto3

# Initialize CloudWatch client
cloudwatch = boto3.client("cloudwatch", region_name="us-east-2")

# Push a fake high temperature datapoint (above alarm threshold of 75°C)
cloudwatch.put_metric_data(
    Namespace="DatabaseMonitoring",
    MetricData=[
        {
            "MetricName": "DatabaseTemperature",
            "Value": 80,  # High value to trigger alarm
            "Unit": "None",
            "Dimensions": [
                {
                    "Name": "InstanceId",
                    "Value": "simulated-db-1"  # use the same dimension as your Alarm.py
                }
            ]
        }
    ]
)

print("✅ Sent test datapoint: DatabaseTemperature = 85°C")