# s3-upload-lambda-sns
This lambda function is triggered by S3 bucket upload of an mp3 file, and then sends email notification to the specified email address.
<br /><br />
<img src="https://github.com/MSebastian2021/s3-upload-lambda-sns/blob/main/images/lambda01.jpg">
<br /><br />
<b>Step 1.</b> Create the S3 Bucket where you will upload your mp3 file.
<br />
<img src="https://github.com/MSebastian2021/s3-upload-lambda-sns/blob/main/images/lambda02.jpg">
<br /><br />
<b>Step 2.</b> Create your <a href="https://github.com/MSebastian2021/s3-upload-lambda-sns/blob/main/lambda_function.py">lambda function</a> in AWS
<br />
<b>Step 3.</b> Create SNS topic, and make the subscription
<br />
<img src="https://github.com/MSebastian2021/s3-upload-lambda-sns/blob/main/images/lambda03.PNG">
<br /><br />
<b>Step 4.</b> Upload a file to the S3 Bucket, and check the specified email destination
<br />
<img src="https://github.com/MSebastian2021/s3-upload-lambda-sns/blob/main/images/lambda06.jpg">
<br /><br />
You can also check the logs:
<br />
<img src="https://github.com/MSebastian2021/s3-upload-lambda-sns/blob/main/images/lambda04.PNG">
<br />
<img src="https://github.com/MSebastian2021/s3-upload-lambda-sns/blob/main/images/lambda05.PNG">
