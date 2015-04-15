#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    return


def process_map(filename):
    users = set() #create empty set, stores each value once
    for event, element in ET.iterparse(filename): #looping through elements
        if 'uid' in element.attrib: #we search for UID attribute
            users.add(element.attrib['uid']) # we add to set the UID, 

    return users


def test():

    users = process_map('map.osm')
    pprint.pprint(users)
 



if __name__ == "__main__":
    test()