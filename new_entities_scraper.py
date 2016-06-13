import urllib2
import time
from bs4 import BeautifulSoup as bsoup
from bs4 import BeautifulSoup
from yaml import load, Loader
import requests as rq
import re



#find people tweeting about civic tech
#('civictech' '#civictech' 'civic tech' 'civictechnology' 'civic technology')
#use keyword scraper

#grab twitter handle
#if 

base_url = ""
r = rq.get(base_url)
soup = bsoup(r.text, "lxml")