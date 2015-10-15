# -*- coding: utf-8 -*-
"""
Billboard Analysis
Looking at salient features in billboard music data
Created on Wed Oct 14 20:09:35 2015

@author: guiltyspark
"""
from collections import defaultdict

#Step 1: Go through and collect each album and it's position on the billboard
# Albums{(Album Name, Artist Name)}: {billboard rank:, billboard dates: }
# Artist{Artist Name}: {albums: }

Artists = defaultdict(set) 
Albums = defaultdict(dict)

start_date = date(2000,1,1)
end_date = date(2000,12,31)
single_date = start_date

def daterange(start_date, end_date, step=1):
    for n in range(0,int ((end_date - start_date).days), step):
        yield start_date + timedelta(n)


for single_date in daterange(start_date,end_date, 7):
    with open('billboard_data/'+str(single_date), 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        for idx, row in enumerate(csvreader):
            my_artist = row[1]
            my_album = row[0]
            Artists[my_artist].add(my_album)    
            if 'billboard_rank' not in Albums[(my_album, my_artist)]:
                Albums[(my_album, my_artist)]['billboard_rank'] = list()
                Albums[(my_album, my_artist)]['billboard_dates'] = list()
            Albums[(my_album, my_artist)]['billboard_rank'].append(idx)
            Albums[(my_album, my_artist)]['billboard_dates'].append(single_date)
                

    