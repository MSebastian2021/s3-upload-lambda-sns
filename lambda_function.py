import urllib.parse
import boto3

print('Loading function')
sns = boto3.client('sns', region_name='eu-west-3')


def lambda_handler(event, context):
    '''
    This lambda function is triggered upon upload of mp3 file to a specified bucket,
    and sends email notification, with details of the upload.
    '''
    
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        message ="Uploaded file, " + key + " to S3 bucket, " + bucket
        response = sns.publish(
        TopicArn='insert your topic arn here',
        Message= message,
        Subject='MP3 file upload'
         )
        
        print ("File uploaded: " + key)
        return response
         
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
