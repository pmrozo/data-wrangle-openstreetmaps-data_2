#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
The output should be a dictionary with the tag name as the key
and number of times this tag can be encountered in the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.ElementTree as ET
import pprint

def count_tags(filename):
    listaTagow = {} #we define empty dictionary with taglist
    for event, elem in ET.iterparse(filename): # we monitor for events like finding a tag in iterative parsing
        if elem.tag not in listaTagow: # we check if the tag is new, found for the first time
            listaTagow[elem.tag] = 1 #we create new key with value =1, because this is the first tag encountered
        else:
            listaTagow[elem.tag] += 1 #we had this key in dictionary so we increment the quantity

    return listaTagow 


def test():

    tags = count_tags('map.osm')
    pprint.pprint(tags)


    

if __name__ == "__main__":
    test()