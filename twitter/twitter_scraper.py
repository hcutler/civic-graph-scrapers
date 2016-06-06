# create day, month, year vars to name output file
import datetime
import tweepy
from twython import Twython

now = datetime.datetime.now()
day=int(now.day)
month=int(now.month)
year=int(now.year)

# add your OAuth tokens
t = Twython(app_key= 'U7BuPNF1Pop5IJEwF0AeHHCX6', #REPLACE 'APP_KEY' WITH YOUR APP KEY, ETC., IN THE NEXT 4 LINES
    app_secret= 'vWuXISxK4DW55A9ws0E62mVaC0UOCMrvJcHfCLVDHzlJF9QFsj',
    oauth_token= '2889424109-TndbOrkSwl1o222aG0X6cnKDcKuk0y9WtmIoXXe',
    oauth_token_secret='ebXw39R7AfSeWmqfF1hM4d8Ph7javEGwZA0ciMKzlp1RV')


users = t.lookup_user(screen_name = 'hannahrcutler')

# initialize output file

outfn = "twitter_user_data_%i.%i.%i.txt" % (now.month, now.day, now.year)

# set variables
# fields = "id screen_name name created_at url followers_count friends_count statuses_count \
#     favourites_count listed_count \
#     contributors_enabled description protected location lang expanded_url".split() 

fields = "id screen_name name created_at url followers_count friends_count statuses_count description location lang expanded_url".split()

outfp = open(outfn, "w")
# outfp.write(str.join(fields, "\t") + "\n")  # header

for entry in users:
    # screen_name = str(entry['screen_name'])
    # print type(screen_name)
    
    timeline = t.get_home_timeline()
    # print timeline
    # print t.get_user_timeline(screen_name)
    #statuses = get_list_statuses(entry)
    # print entry['status']['text']

    i = 0
    while i < len(timeline):
        print timeline[i]['text']
        i+=1
    #CREATE EMPTY DICTIONARY
    r = {}

    for f in fields:
        r[f] = ""
    #ASSIGN VALUE OF 'ID' FIELD IN JSON TO 'ID' FIELD IN OUR DICTIONARY
    r['id'] = entry['id']
    #SAME WITH 'SCREEN_NAME' HERE, AND FOR REST OF THE VARIABLES
    r['screen_name'] = entry['screen_name']
    r['name'] = entry['name']
    r['created_at'] = entry['created_at']
    r['url'] = entry['url']
    r['followers_count'] = entry['followers_count']
    r['friends_count'] = entry['friends_count']
    r['statuses_count'] = entry['statuses_count']
    # r['favourites_count'] = entry['favourites_count']
    # r['listed_count'] = entry['listed_count']
    # r['contributors_enabled'] = entry['contributors_enabled']
    r['description'] = entry['description']
    # r['protected'] = entry['protected']
    r['location'] = entry['location']
    r['lang'] = entry['lang']
    
    #NOT EVERY ID WILL HAVE A 'URL' KEY, SO CHECK FOR ITS EXISTENCE WITH IF CLAUSE
    if 'url' in entry['entities']:
        r['expanded_url'] = entry['entities']['url']['urls'][0]['expanded_url']
    else:
        r['expanded_url'] = ''
    print r
    #CREATE EMPTY LIST
    lst = []
    #ADD DATA FOR EACH VARIABLE
    for f in fields:
        lst.append(unicode(r[f]).replace("\/", "/"))
    #WRITE ROW WITH DATA IN LIST
    #outfp.write(str.join(lst, "\t").encode("utf-8") + "\n")
 
outfp.close()    