import requests
import boto3
import os, json

r = requests.get('http://www.the-star.co.ke/api/mobile/views/mobile_app?args[0]=24&limit=50')

feed = r.json()
articles = []

for article in feed:
    articles.append({'node': article})

data = {
    'nodes': articles,
    'tags' : []
}


s3 = boto3.client(
    's3',
    aws_access_key_id=os.environ['MORPH_AWS_ACCESS_KEY'],
    aws_secret_access_key=os.environ['MORPH_AWS_SECRET_KEY'],
    region_name='eu-west-1'
)

s3.put_object(
    Bucket='cfa-healthtools-ke',
    ACL='public-read',
    Key='starhealth-news.json',
    Body=json.dumps(data)
)
