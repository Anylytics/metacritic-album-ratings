# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:15:12 2015

@author: guiltyspark
"""
import csv
from collections import defaultdict
import datetime
import matplotlib.pyplot as plt
import numpy as np
import itertools
import pprint

pp = pprint.PrettyPrinter(indent=4)
artists = defaultdict(list) 

# Read The Data 
for i in range(65):
    with open('metacritic_data/'+str(i), 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            artist = row[0]
            data = {'artist': artist, 'album': row[1], 'date': datetime.datetime.strptime(row[2], '%b %d, %Y').date(), 'metascore': int(row[3]), 'userscore': row[4] }
            artists[artist].append(data) 

del artists["Various Artists"]

sorted_artists = sorted(artists, key=lambda k: len(artists[k]), reverse = True)
    

num_albums = [len(artists[x]) for x in artists]
sorted_num_albums = sorted(num_albums)


yvals=np.arange(len(sorted_num_albums))/float(len(sorted_num_albums))
plt.plot( sorted_num_albums, yvals )


#For each artist, score each album as, y=rating of this album, x = average rating of previous two

for artist, albums in artists.iteritems():
    if len(albums) > 2:
        for i in range(len(albums)-2):
            albums[i]['average-score'] = np.mean([albums[i+1]['metascore'], albums[i+2]['metascore']])


#Now get all the albums that have an average score
selected_albums_temp = map(lambda k: [x for x in k if 'average-score' in x], artists.values())
selected_albums = list(itertools.chain.from_iterable(selected_albums_temp))

x_vals = [x['average-score'] for x in selected_albums]
y_vals = [y['metascore'] for y in selected_albums]

plt.scatter(x_vals, y_vals)

#Calculate the big movers and shakers
for album in selected_albums:
    album['diff'] = album['metascore'] - album['average-score']
    
sorted_albums = sorted(selected_albums, key=lambda k: k['diff'], reverse = True)
