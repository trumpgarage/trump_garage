import tweepy
import csv
import pandas as pd
import re

##Inputs
filename = 'gj.csv'
hashtag = '#giletsjaunes'

####input your credentials here
consumer_key = 'UXxQLk7RJd3xP3cAh9unhKAzQ'
consumer_secret = '60T2JjYzmpCKSfcS5fCQQRnVeSc6TeXNiU655fxdGwIxskuMX3'
access_token = '1089160091671162881-njrgdezc4foUK8n5AADY0GjF4A2aNC'
access_token_secret = 'vsJTEeQt04UwISsbb76MCuPZhMKyewuyDPVurayOGJcmh'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open(filename, 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
i = 0
re.DOTALL
for tweet in tweepy.Cursor(api.search,q=hashtag,count=10,
                           lang="fr",
                           since="2018-12-01").items():
    i+=1 
    #print (tweet.created_at, tweet.text)
    raw_text = tweet.text
    raw_text = re.sub(r'(\s)@\w+', r'\1', raw_text, 1)
    raw_text = re.sub(r'(\s)https\w+', r'\1', raw_text)
    raw_text = re.sub(r'(\S)https\w+', r'\1', raw_text)
    raw_text = re.sub(r'(\s)https\S+', r'\1', raw_text)
    raw_text = re.sub(r'(\s)RT\w+', ' ', raw_text)    
    raw_text = re.sub('RT', '', raw_text)
    raw_text = re.sub(r'(\s):\s+', '', raw_text, 1)
    print(raw_text)
    #csvWriter.writerow([ tweet.text.encode('utf-8')])
    if i >= 1000 :
        break

