# Import packages and config
from tweepy import OAuthHandler, API
from config import consumer_key, consumer_secret, access_token, access_token_secret, app_pw, from_mail, to_mail
import smtplib
import re
from email.mime.text import MIMEText

# Authenticate Tweepy connection
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

# Login & Authentification of email
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login(from_mail, app_pw)

# Open log
f = open('log.txt', 'r+')
logged_tweets = [line for line in f.readlines()]

# Getting tweets
miranda_tweets = api.user_timeline('@Lin_Manuel')

# If tweet matches, checking log, adding if new, and sending.
for status in miranda_tweets:
    if re.search("(.*morning|.*night)", status.text) != None:
        if status.id_str not in logged_tweets:
            f.writelines("\n" + status.id_str)
            msg = MIMEText("Good Morning / Good Night: \nhttps://www.twitter.com/lin_manuel/statuses/" + status.id_str)
            msg['From'] = from_mail
            msg['To'] = to_mail
            s.sendmail(from_mail, to_mail, msg.as_string())
# Terminating the session 
s.quit() 
f.close()