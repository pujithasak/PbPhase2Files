from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3405966891-r5CNBJTzrgjQtudAujzm2nhCEkumcriZeUP0ch2"
access_token_secret = "GQvL88RMQnn1W2leFsV1YnFJt3CyHmAla2Cj7d9nOnO4J"
consumer_key = "ZP7bI9huRiUCF6g8lcohyqaV0"
consumer_secret = "qQVTCyZX6jU1SvcLDI2k0SNKO8aou4MRfuObnHYJQQoY02Rt2v"



#This is a basic listener that just prints received tweets to stdout.
class TwitterStreamer():
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        stream = Stream(auth, listener)

        
        stream.filter(track=hash_tag_list)



class StdOutListener(StreamListener):
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a+') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)



 
if __name__ == '__main__':
 

    hash_tag_list = ['iphone','Samsung','Moto','Redmi','Xiaomi','Nokia','lenovo','oppo','OnePlus','BlackBerry','HTC','phones','ipads','cell phone','smart phones','mobile phones']
    fetched_tweets_filename = "importedtweetsdata.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
