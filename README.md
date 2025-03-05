# GetRateCodeFromSCUTO
A pithy codebase for retrieving rate code from service code, usage type, operation found in usage lines of Workload estimates in AWS Pricing Calculator

# Instructions

1. Set up your AWS environment to use a profile from either `~/.aws/credentials` or `~/.aws/config`.
2. Enter the profile name in the following line found in `main.py`.

```
session = boto3.Session(profile_name="default", region_name="us-east-1")
```
3. Create an estimate in Pricing Calculator at https://calculator.aws/
4. Save the estimate and copy the estimate URL.
5. 
