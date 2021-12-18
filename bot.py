import tweepy
import time

# user secrets
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# api.update_status('Twitter bot reporting in live')

# print(tweets[0].text)
FILE_NAME = 'seen.txt'

def read_last_seen(FILE_NAME):
    reader = open(FILE_NAME, 'r')
    last_seen_id = int(reader.read().strip())
    reader.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    writer = open(FILE_NAME, 'w')
    writer.write(str(last_seen_id))
    writer.close()
    return 

def reply():
    tweets = api.mentions_timeline(since_id=read_last_seen(FILE_NAME), tweet_mode='extended')
    assessment_form = 'https://docs.google.com/forms/d/e/1FAIpQLSegYGV61q18f2BINqrmGTnYYSAPWl6BaloOa8ZSHsNWGp7Qsg/viewform?vc=0&c=0&w=1&flr=0&usp=mail_form_link\n'
    scheduling_form = 'https://docs.google.com/forms/d/e/1FAIpQLSfSZjA69j-BGIn0oB-DUO56Ue6APpBgiBggPHd2Y3SdfJyQaA/viewform?vc=0&c=0&w=1&flr=0&usp=mail_form_link\n'

    for tweet in reversed(tweets):
        if '#hearmeout' in tweet.full_text.lower():
            print(str(tweet.id) + ' - ' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " Don't worry help is on the way :)\n" 
                + 'Unsure?: ' + assessment_form 
                + 'Book an appointment with our volunteers: ' + scheduling_form
                + ' ' + str(time.time()))
            tweet_id = str(tweet.id)
            store_last_seen(FILE_NAME, tweet_id)

while True:
    reply()
    time.sleep(3)