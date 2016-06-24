import urllib2
import time
from bs4 import BeautifulSoup
import yaml
import json
import re
import string
from collections import Counter
import pprint
from collections import OrderedDict


# def get_entities(string):
#   re.findall('([A-Z][\w-]*(?:\s+[A-Z][\w-]*)+)', string)


ent_list = []
word_dict={}

with open('all_content.txt', 'r') as f:
  read_data = f.read()
  entities = re.findall('([A-Z][\w-]*(?:\s+[A-Z][\w-]*)+)', read_data)
  for e in entities:
    e.strip('Share')
    e.strip('Share\n\n\nShare')
    e.strip('Share on Twitter')
    e.strip('Facebook\n\n\nShare')
    e.strip('Twitter\n\n\n')
    e.strip('Share by Email')
    e.strip('Topics  First Post')
    e.replace('\n',"")
    
    word_dict[e] = 0
  for e in entities:
      word_dict[e] += 1

  genexp = ((k, word_dict[k]) for k in sorted(word_dict, key=word_dict.get, reverse=True))
  for k, v in genexp:
    print k, v


  # print sorted(word_dict)
  # print word_dict.keys()
  # print word_dict.values()
    #st.append(e)

#pprint.pprint(Counter(ent_list))




