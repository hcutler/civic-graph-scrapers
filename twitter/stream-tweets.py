# created on Sat Jun 07 12:52:46 2014

# @author Martez Mott memott@uw.edu

# revisions 3-9-15 by: Oliver Haimson ohaimson@uci.edu



#### SET YOUR SEARCH TERMS AND PARAMETERS HERE ####

search_term = ["#datascience"]
#search_term = ["yesallwomen", "yesallwhitewomen", "cisgaze", "notallmen"]

maximum_number_of_tweets = 2        # set the maximum number of tweets
# endTime = "06 30 17:50"              # set the end time in this format mm dd hh:mm

###################################################


import sys, pprint, json, csv, time, tweepy
import datetime
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.api import API
from tweepy.streaming import StreamListener
import nltk
from nltk.tokenize import *

# obtain your access tokens at apps.twitter.com and paste them here
# CODE WILL NOT WORK UNLESS YOU DO THIS :)
# ckey = 'UWnpS1uUr2IaQ3WlmCP0V5LA7'
# csecret = 'qtd11iCpdGgUpztsdxWpfCMKwYZqKO6NkSgZo1tVmfF0zQFqGY'
# atoken = '2559138218-Zz7Hf773JPTIAOMC58Lr3tCALO9WWx63EFjRAoO'
# asecret = 'zK6KOPBv1GMTkpt1xxbXkuP3STtUVyOdymxpfoRQd0z8B'

ckey = 'U7BuPNF1Pop5IJEwF0AeHHCX6'
csecret = 'vWuXISxK4DW55A9ws0E62mVaC0UOCMrvJcHfCLVDHzlJF9QFsj'
atoken = '2889424109-TndbOrkSwl1o222aG0X6cnKDcKuk0y9WtmIoXXe'
asecret = 'ebXw39R7AfSeWmqfF1hM4d8Ph7javEGwZA0ciMKzlp1RV'

now = datetime.datetime.now()
hour = int(now.hour)
minute = int(now.minute) + 10
day=int(now.day)
month=int(now.month)
year=int(now.year)

endTime = str(month) + " " + str(day) + " " + str(hour) + ":" + str(minute)


# authenticate
def authenticate():
    if ckey==' ' or csecret==' ' or atoken==' ' or asecret==' ':
        print("Please obtain your access tokens at apps.twitter.com and paste them into the code!")
        sys.exit()
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    return auth        

# a class inherited from the StreamListner class in the Twitter API
# This class will print out a tweet in the on_status function

class view_and_save_stream(StreamListener):

    def __init__(self, api=None):
        self.api = api or API()
        self.current_number_of_tweets = 0

        # open the file where we're going to save the data
        self.file = open('data'+time.strftime("%m%d%H%M")+".csv", 'w') # name the file data + the current date and time, to eliminate overwriting         
        self.writer = csv.writer(self.file)
        # write the header row
        self.writer.writerow(('user', 'location', 'coordinates', 'text', 'time', 'hashtags', 'user mentions'))   

    # when a new tweet is posted, this function is automatically called    
    def on_status(self, status):

        # format the text fields as unicode
        clean_name = status.user.screen_name.encode('utf-8')
        clean_location = status.user.location.encode('utf-8')
        clean_tweet = status.text.encode('utf-8')

        # get rid of newlines to eliminate issues with csv formatting
        clean_tweet = clean_tweet.replace('\n', '')

        # find hashtags and user mentions in tweets
        hashtags = getHashtags(clean_tweet)
        user_mentions = getUserMentions(clean_tweet)
        
        # determine if the tweet is geotagged. If it is, collect the coordinates
        if isinstance(status.coordinates, dict):
            coord = status.coordinates["coordinates"]
        else: coord = "None"

        # print each tweet and write it to the csv file
        self.writer.writerow((clean_name, clean_location, coord, clean_tweet, status.created_at, hashtags, user_mentions))     # write the data to be stored in the file
        print 'User: {0}, Location: {1}, Coordinates: {2}, Tweet: {3}, Time: {4}, Hashtags: {5}, User Mentions: {6}'.format(clean_name, clean_location, coord, clean_tweet, status.created_at, hashtags, user_mentions)
        print str(self.current_number_of_tweets+1)+" / "+str(maximum_number_of_tweets)
        print '------------------------'

        # continue running the script until we reach the maximum number of tweets or go passed the end time
        self.current_number_of_tweets = self.current_number_of_tweets + 1       # each time a tweet is collected, increment the counter
        currentTime = time.strftime("%m %d %H:%M")
        if ( self.current_number_of_tweets < maximum_number_of_tweets) and (currentTime < endTime):
            return True
        else:
            self.file.close()
            print '......end of stream'
            return False


# a function to view tweets containing the search term, and save them to a csv file    
def view_and_save_tweets(search_term):
    auth = authenticate()
    print '......getting tweets'
    twitter_stream = Stream(auth, view_and_save_stream())
    twitter_stream.filter(track=search_term)
    return

# a function to extract hashtags from tweet text
def getHashtags(tweet):
    hashtags=""
    x = WhitespaceTokenizer().tokenize(tweet)
    for word in x:
        if word[0]=="#":
            hashtags=hashtags+word+" "
    return hashtags

# a function to extract user mentions from tweet text
def getUserMentions(tweet):
    user_mentions=""
    x = WhitespaceTokenizer().tokenize(tweet)
    for word in x:
        if word[0]=="@":
            user_mentions=user_mentions+word[1:].replace(":","")+" "
    return user_mentions



######################################################
# run the code using the search term(s) provided above
view_and_save_tweets(search_term)

    





