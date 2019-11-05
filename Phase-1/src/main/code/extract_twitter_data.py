twitterAccessToken = "1039581348267216896-X356h5IuiIWuiHbIoe6Czq4"
twitterAccessTokenSecret = "wlUWfSuJnLGlczTaKN1HBlDr6EMrBHeegTG7hKB"
myConsumerKey = "Y3ndR0ynAmxZhe39UORvNM"
myConsumerSecret = "gIKPFvZKJk0EXMyoFSn3TZOG8LUGAuhrOxOwDRSZZV"

import tweepy
from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_data(self, retrievedData):
        
        print retrievedData
        return True
        

    def on_error(self, retrievedStatus):
        print retrievedStatus


if __name__ == '__main__':
    
    listener = StdOutListener()
    from tweepy import OAuthHandler
    oAuth = OAuthHandler(myConsumerKey, myConsumerSecret)
    oAuth.set_access_token(twitterAccessToken, twitterAccessTokenSecret)
    from tweepy import Stream
    #tweetCount = 3
    
    stream = Stream(oAuth, listener)
    stream.filter(track=['bitcoin', 'ethereum', 'ripple', 'litecoin', 'stellars'])
    #for tweet in iterator:
        
        #tweetCount -= 1
        
            

