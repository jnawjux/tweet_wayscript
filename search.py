# Import packages and config
from tweepy import OAuthHandler, API
from config import consumer_key, consumer_secret, access_token, access_token_secret
import re

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = API(auth)

r = re.compile("(.*morning|.*night)")
 
miranda = api.user_timeline('@Lin_Manuel')
tweets = [status.text for status in miranda]
newlist = list(filter(r.match, tweets))
for t in newlist:
    print(t)
