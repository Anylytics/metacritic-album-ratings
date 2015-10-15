# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 13:08:06 2015

@author: guiltyspark
"""

from lxml import html
import requests
import bs4
import csv
from datetime import timedelta, date

start_date = date(2011,1,1)
end_date = date(2015,12,31)

def daterange(start_date, end_date, step=1):
    for n in range(0,int ((end_date - start_date).days), step):
        yield start_date + timedelta(n)

for single_date in daterange(start_date,end_date, 7):
   #for index in xrange(50,65):
    #print index
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    
    
    page = requests.get('http://www.billboard.com/charts/top-album-sales/'+str(single_date), headers=hdr)
    
    soup = bs4.BeautifulSoup(page.text)
    rows = soup.find_all("div", class_="row-title")
    
    
    billboard = list()
    
    for row in rows:
        everything = row.get_text().encode('utf-8').strip(' \t\n\r').split("\n")
        album = everything[0].strip(' \t\n\r')
        artist = everything[-1].strip(' \t\n\r')
        billboard.append([album, artist])
    
    
    with open('billboard_data/'+str(single_date), 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerows(billboard)

