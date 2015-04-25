#!/usr/bin/python

import sys

current_url_hits = 0
most_popular_url = ''
most_popular_url_hits = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        if current_url_hits > most_popular_url_hits:
            most_popular_url = oldKey
            most_popular_url_hits = current_url_hits
        oldKey = thisKey
        current_url_hits = 0

    oldKey = thisKey
    current_url_hits += 1

if current_url_hits > most_popular_url_hits:
    most_popular_url = oldKey
    most_popular_url_hits = current_url_hits

if most_popular_url:
    print most_popular_url, "\t", most_popular_url_hits

