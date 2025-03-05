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
5. Go to authenticated Pricing Calculator on Billing and Cost Management console.
6. Create a new Workload estimate. Refer: https://docs.aws.amazon.com/cost-management/latest/userguide/pc-workload-estimate.html.
7. Add previously saved estimates to my workload estimate. Refer: https://docs.aws.amazon.com/cost-management/latest/userguide/pc-create-workload-previous-url.html.
8. Once usage is added, then run this program (`python main.py`), and pass the GUID of the Workload estimate to the program. You can find the GUID under 'Estimate Id' column on Saved Estimate page or from the browser URL. This GUID is also part of the estimate ARN.
