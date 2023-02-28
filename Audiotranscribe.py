import json
import os
import boto3
import pyttsx3
import aws
import time
import random
from startRecording import usrQuestionFile
from urllib.parse import urlparse

# TODO
# Make use of cloud storage so file paths work across different devices

# ---Initialization--- #
os.environ['AWS_ACCESS_KEY_ID'] = 'Enter your key'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'enter your key'

# initializes engine for speech
engine = pyttsx3.init()
# random number for file name to avoid repeting name error
randomNumber = random.randint(0, 5000)

transcribe = boto3.client('transcribe', region_name='us-east-2')
s3 = boto3.client('s3')
bucket_name = 'audiotest.01'
file_name = usrQuestionFile
s3.upload_file(file_name, bucket_name, file_name)

job_name = 'TEST' + str(randomNumber)
print(job_name)
job_uri = f's3://{bucket_name}/{os.path.basename(file_name)}'
language_code = 'en-US'

OutputKey = 'transcriptions/{}.json'.format(job_name)


job_params = {
    'TranscriptionJobName': job_name,
    'Media': {
        'MediaFileUri': f's3://{bucket_name}/{file_name}'
    },
    'OutputBucketName': 'voice-text-output',  # change this
    'OutputKey': OutputKey,  # change this
    'LanguageCode': language_code
}

transcribe.start_transcription_job(**job_params)

while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    engine.say("Transcribing your speech to text")
    engine.runAndWait()
    print("Waiting for job completion...")
    time.sleep(10)

bucket_name = 'voice-text-output'
key = 'transcriptions/{}.json'.format(job_name)
local_file_path = '/Users/junyanglu/Downloads/{}.json'.format(job_name)

if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
    s3.download_file(bucket_name, key, local_file_path)
    print("Output file downloaded successfully!")
else:
    engine.say("Failed to transcribe audio to text")
    print("Transcription job failed!")


'''folder_path = '/Users/eric/Downloads'
files = os.listdir(folder_path)
json_files = [f for f in files if f.endswith('.json')]

n = len(json_files)-1'''

filename = "/Users/junyanglu/Downloads/{}.json".format(job_name)

with open(filename, 'r') as f:
    data = json.load(f)

a = ','
list = data['results']['transcripts']
output = list[0]['transcript']

with open('/Users/junyanglu/Downloads/text.txt', 'w') as f:
    f.write(output)

with open('/Users/junyanglu/Downloads/text.txt', "r") as file:
    answers = file.read()
