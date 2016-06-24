from lxml import etree
import lxml
import os
from os.path import join, getsize
from xml.etree.ElementTree import ElementTree
import csv
from csv import DictWriter
import sys

reload(sys)
sys.setdefaultencoding("utf-8")



companyrows = []


#parse XML files to extract data
for root, dirs, files in os.walk('990-data/'):
  for filename in files:
    if filename.endswith('.xml'):
      fullpath = os.path.join(root, filename)
      f = open(fullpath)
      doc = etree.parse(f)
      name = doc.xpath('//ReturnHeader/Filer/Name/BusinessNameLine1')
      location = doc.xpath('//ReturnHeader/Filer/Address')
      
      
      for n in name:
        print n

      # for i in range(len(name)):
        # print name[i].text