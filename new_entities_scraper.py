import urllib2
import time
from bs4 import BeautifulSoup as bsoup
from bs4 import BeautifulSoup
from yaml import load, Loader
import requests as rq
import re


#get contents of Tandon School of Engineering NYU page
base_url = "http://engineering.nyu.edu/people?"
r = rq.get(base_url)
soup = bsoup(r.text, "lxml")