import urllib2
import time
from bs4 import BeautifulSoup as bsoup
from bs4 import BeautifulSoup
from yaml import load, Loader
import requests as rq
import re


#get contents of Tech President's archives
base_url = "http://techpresident.com/topics/"
r = rq.get(base_url)
soup = bsoup(r.text, "lxml")

topics = ['revolution', 'obama-2012', 'malcolm-gladwell',
          'hacktivism', 'facebook', 'online-organizing',
          'wegov', 'backchannel', 'civic-hacking'] 

morelinks = ['http://techpresident.com/techpresident-topics/debates-20',
              'http://techpresident.com/techpresident-topics/hip-or-hype',
              'http://techpresident.com/techpresident-topics/grassrootsiness',
              'http://techpresident.com/techpresident-topics/email-watch',
              'http://techpresident.com/techpresident-topics/blogging',
              'http://techpresident.com/techpresident-topics/occupywallst',
              'http://techpresident.com/techpresident-topics/gop-2012',
              'http://techpresident.com/techpresident-topics/design']

links = []
for t in topics:
  url = base_url + t
  links.append(url)

for m in morelinks:
  links.append(m)

i = 0
for l in links:
  html_doc = urllib2.urlopen(l).read()

  fname = 'topicpage_' + str(i)
  i += 1

  with open(fname, "w") as html_file:
    html_file.write(html_doc)



# contents = soup.findAll('div', attrs={"id": "topic-background"})
# print contents
