import json
import os
from datetime import datetime, timedelta

import boto3
from botocore.exceptions import NoCredentialsError, ProfileNotFound, ClientError

try:
    # change the profile name per your ~/.aws/credentials or ~/.aws/config
    session = boto3.Session(profile_name="default", region_name="us-east-1")
except (NoCredentialsError, ProfileNotFound):
    print('AWS credentials not found or improperly configured.')
except Exception:
    print('Error with setting up AWS session.')


def get_cost_and_usage():
    client = boto3.client('ce')
    end_date = datetime.today().replace(day=1)
    start_date = (end_date - timedelta(days=1)).replace(day=1)

    response = client.get_cost_and_usage(
        TimePeriod={
        'Start': start_date.strftime('%Y-%m-%d'),
        'End': end_date.strftime('%Y-%m-%d')
        },
        Granularity='MONTHLY',
        Metrics=['UNBLENDED_COST'],
        Filter={
            'And': [
                {
                    'Dimensions': {
                        'Key': 'SERVICE',
                        'Values': ['Amazon DynamoDB']
                    }
                },
                {
                    'Dimensions': {
                        'Key': 'REGION',
                        'Values': ['us-east-1']
                    }
                }
            ]
        }
    )

    for result in response['ResultsByTime']:
        print(f"Time Period: {result['TimePeriod']['Start']} to {result['TimePeriod']['End']}")
        print(f"Unblended Cost: {result['Total']['UnblendedCost']['Amount']} {result['Total']['UnblendedCost']['Unit']}")


def get_usage_forecast():
    
    start_date = datetime.today() + timedelta(days=1)
    end_date = start_date + timedelta(days=10)
    custom_endpoint_url = 'https://ce.us-east-1.amazonaws.com'
    region = 'us-east-1'
    client = boto3.client('ce',
                          region_name=region, 
                          endpoint_url=custom_endpoint_url)

    response = client.get_usage_forecast(
        TimePeriod={
        'Start': start_date.strftime('%Y-%m-%d'),
        'End': end_date.strftime('%Y-%m-%d')
        },
        Granularity='DAILY',
        Metric='USAGE_QUANTITY',
        Filter={
            'And': [
                {
                    'Dimensions': {
                        'Key': 'SERVICE',
                        'Values': ['Amazon DynamoDB']
                    }
                },
                {
                    'Dimensions': {
                        'Key': 'USAGE_TYPE',
                        'Values': ['WriteCapacityUnit-Hrs']
                    }
                }
            ]
        },
        BillingViewArn='arn:aws:billing::<account-id>:billingview/primary'
    )

    for result in response['ForecastResultsByTime']:
        print(f"Time Period: {result['TimePeriod']['Start']} to {result['TimePeriod']['End']}")
        print(f"Mean value: {result['MeanValue']}")


if __name__ == "__main__":
    get_cost_and_usage()
    get_usage_forecast()
