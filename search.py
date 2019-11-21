# Import packages and config
from tweepy import OAuthHandler, API
from config import consumer_key, consumer_secret, access_token, access_token_secret, app_pw, from_mail, to_mail
import re

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)

r = re.compile("(.*morning|.*night)")
 
miranda = api.user_timeline('@Lin_Manuel')
tweets = [status.text for status in miranda]
newlist = list(filter(r.match, tweets))
message =  ", ".join(newlist)

import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login(from_mail, app_pw) 
  
  
# sending the mail 
s.sendmail(from_mail, to_mail, message.encode("utf8")) 
  
# terminating the session 
s.quit() 