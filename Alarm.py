import boto3

# Initialize clients
cloudwatch = boto3.client("cloudwatch", region_name="us-east-2")
sns = boto3.client("sns", region_name="us-east-2")

# 1. Create SNS Topic
topic = sns.create_topic(Name="db-temp-alerts")
topic_arn = topic["TopicArn"]

# 2. Subscribe your email/phone
sns.subscribe(
    TopicArn=topic_arn,
    Protocol="email",  # "sms" also possible
    Endpoint="surendra.k.s.333@gmail.com" # replace with your email or phone number
)

# 3. Create a CloudWatch Alarm
cloudwatch.put_metric_alarm(
    AlarmName="HighDBTemperature",
    ComparisonOperator="GreaterThanThreshold",
    EvaluationPeriods=1,
    MetricName="DatabaseTemperature",
    Namespace="DatabaseMonitoring",
    Period=60,
    Statistic="Average",
    Threshold=70,  # threshold in Celsius
    ActionsEnabled=True,
    AlarmActions=[topic_arn],
    AlarmDescription="Alarm when database CPU temperature exceeds 75°C",
    Unit="None"
)