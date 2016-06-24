import urllib2
import csv
import time
from bs4 import BeautifulSoup
# from collections import deque
import locale


#read in contents of csv file
entities = []
with open('civic-tech-inform.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ' ', quotechar='|')
    # spamreader.next()
    for line in spamreader:
        entities.append(' '.join(line))

    for e in entities:
        print e




    # for row in spamreader:
    #     print ' '.join(row)
