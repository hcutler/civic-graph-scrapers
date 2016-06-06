import sys
import urllib
import string
import simplejson
import sqlite3

import time
import datetime
from pprint import pprint

import sqlalchemy
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Unicode #
from sqlalchemy import Text #

from sqlalchemy import DECIMAL
from sqlalchemy import Unicode


from sqlalchemy.sql import join
from types import *

from datetime import datetime, date, time

ids = ['%23 #civictech'] #ENTER YOUR SEARCH TERM DIRECTLY AFTER THE 23

from twython import Twython

t = Twython(app_key= 'U7BuPNF1Pop5IJEwF0AeHHCX6',
    app_secret= 'vWuXISxK4DW55A9ws0E62mVaC0UOCMrvJcHfCLVDHzlJF9QFsj',
    oauth_token= '2889424109-TndbOrkSwl1o222aG0X6cnKDcKuk0y9WtmIoXXe',
    oauth_token_secret='ebXw39R7AfSeWmqfF1hM4d8Ph7javEGwZA0ciMKzlp1RV')


Base = declarative_base()


class Messages(Base):
    __tablename__ = 'hashtags'
    
    id = Column(Integer, primary_key=True)  
    query = Column(String)
    tweet_id = Column(String) 

    content = Column(Text)
    from_user_screen_name = Column(String)
    from_user_id = Column(String)   


    def __init__(self, query, tweet_id, content, from_user_screen_name, from_user_id): 

        self.query = query
        self.tweet_id = tweet_id
        self.content = content
        self.from_user_screen_name = from_user_screen_name
        self.from_user_id = from_user_id       


    def __repr__(self):
       return "<Organization, Sender('%s', '%s')>" % (self.from_user_screen_name,self.created_at)

def get_data(kid, max_id=None):
    try:
        # d = t.search(q=kid, count = '200', result_type = 'mixed', lang = 'en', max_id = max_id) #RESULT TYPE CAN BE MIXED, RECENT, OR POPULAR
        d = t.search(q=kid, count = '200', result_type = 'recent', lang = 'en', max_id = max_id) #RESULT TYPE CAN BE MIXED, RECENT, OR POPULAR
        
    except Exception, e:
        print "Error reading id %s, exception: %s" % (kid, e)
        return None
    print "d.keys(): ", d.keys()   
    print "######## # OF STATUSES IN THIS GRAB: ", len(d['statuses'])
    #print "max_id VALUE USED FOR THIS GRAB-->", max_id
    return d
    
def write_data(self, d):   

    query = d['search_metadata']['query']
    
    number_on_page = len(d['statuses'])
    ids = []
    for entry in d['statuses']:
        json_output = str(entry)
        tweet_id = entry['id']

        content = entry['text']
        content = content.replace('\n','')      
        from_user_screen_name = entry['user']['screen_name']
        from_user_id = entry['user']['id'] 
        from_user_description = entry['user']['description'] 
        from_user_location = entry['user']['location'] 
  

        source = entry['source']          
      
        print "urls...?....", 
        print "user_mentions...?....", 
        print "hashtags...?....", 
        
      
        updates = self.session.query(Messages).filter_by(query=query, from_user_screen_name=from_user_screen_name,
                content=content).all() 
        
        self.session.commit()
        
      

class Scrape:
    def __init__(self):    
        engine = sqlalchemy.create_engine("sqlite:///db-test", echo=False)  #ENTER NAME OF YOUR DATABASE WHERE DIRECTED
        Session = sessionmaker(bind=engine)
        self.session = Session()  
        Base.metadata.create_all(engine)

    def main(self):
        for n, kid in enumerate(ids):
            print "\rprocessing id %s/%s" % (n+1, len(ids)),
            sys.stdout.flush()


            d = get_data(kid)
            if not d:
                continue	 

            print d['statuses'][0]

            self.session.commit()


        self.session.close()



if __name__ == "__main__":
    s = Scrape()
    s.main()

