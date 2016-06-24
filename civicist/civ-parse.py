import urllib2
import time
from bs4 import BeautifulSoup as bsoup
from bs4 import BeautifulSoup
from yaml import load, Loader
import requests as rq
import re

#get contents of Civicist archives
base_url = "http://civichall.org/topic/first-post/"
r = rq.get(base_url)
soup = bsoup(r.text, "lxml")

page_count_links = soup.find_all("a",href=re.compile(r".*javascript:goToPage.*"))
try: # Make sure there are more than one page, otherwise, set to 1.
    num_pages = int(page_count_links[-1].get_text())
except IndexError:
    num_pages = 29 #29 pages

url_list = ["{}page/{}".format(base_url, str(page)) for page in range(1, num_pages + 1)]

url_list.remove('http://civichall.org/topic/first-post/page/1')

url_list.insert(0, "http://civichall.org/topic/first-post/")


article_links = []

for url in url_list:
  html_doc = urllib2.urlopen(url).read()
  soup = BeautifulSoup(html_doc, "lxml")
  contents = soup.findAll('h2', attrs={"class": "post-title"})
  for link in contents:
    #x = re.search("(?P<url>https?://[^\s]+)", str(link).group("url"))
    link = str(link)
    start = link.find("http") #index of this
    end = link.find('/">')
           
    # print link[start:end]
    article_links.append(link[start:end])

#write article urls to textfile
with open("articles_links.txt", "w") as outfile:
  for x in article_links:
    outfile.write(x +'\n')






#print article_links


    # x = re.findall(r'(https?://\S+)', str(link))
    # print link[9:len(link)-15]

  #get_article_links(html_doc)

#get href links within post-title tags


# def get_article_links(str):
#   soup = BeautifulSoup(str, "lxml")



# for url in url_list:
#   html_doc = urllib2.urlopen(url).read()