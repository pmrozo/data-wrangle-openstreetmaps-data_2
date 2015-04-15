#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import pprint
import re
import codecs
import json
import sys
from pymongo import MongoClient


lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = [ "version", "changeset", "timestamp", "user", "uid"]




# here I take the contenf of a map file, read tags, do some cleaning 
def cleanmyfile(element):
    node = {}
    chars = set('@')
    if element.tag == "node" or element.tag == "way" : #only node and way is checked
        node['id'] = element.attrib['id']
        node['type'] = element.tag
        for tag in element.iter("tag"):
			if tag.attrib['k'] == "source": #my 1st check, if tag's attrib is source then  ido some cleaning
				
				if 'http://ump.waw.pl/' in tag.attrib['v']:
					#print tag.attrib['v']
					tag.attrib['v']='http://ump.waw.pl/'
					print "fixed "+tag.attrib['v']
				
			if tag.attrib['k'] == "email": #my 2nd check, if tag's attrib is email then i check for @ sign 
				
				if any((c in chars) for c in tag.attrib['v']):
					print "checked and ok"+tag.attrib['v']
					return node
				else:
					return None
				
			if 'gmai' in tag.attrib['v']:#my 3 rd check, fix wrong domain, 
				tag.attrib['v']=tag.attrib['v'].replace("gmai", "gmail")
				print "fixed gmail"+tag.attrib['v']
					

					
			if tag.attrib['k'] == "addr:postcode":#my 4 th check, check if there is correct postal code, if not then omit, since we are not interested in other cities
				if ('31-' in tag.attrib['v']) or ('30-' in tag.attrib['v'])or ('32-' in tag.attrib['v']):
					return node
				else:
					print "wrong postalCODE "+tag.attrib['v']
					return None
						# below code comes from lessons
        if 'visible' in element.attrib:
            node['visible'] = element.attrib['visible']
        node['created'] = {}
        for c in CREATED:
            node['created'][c] = element.attrib[c]
        if 'lat' in element.attrib:
            node['pos'] = [float(element.attrib['lat']), float(element.attrib['lon'])]
        if element.find("tag") != None:
            #node['address'] = {}
            for tag in element.iter("tag"):
                if lower_colon.match(tag.attrib['k']) and tag.attrib['k'].startswith("addr:"):
                    if 'address' not in node:
                        node['address'] = {}
                    node['address'][tag.attrib['k'].split(":")[1]] = tag.attrib['v']
                elif lower.match(tag.attrib['k']) and not tag.attrib['k'].startswith("addr:"):
                    node[tag.attrib['k']] = tag.attrib['v']
        if element.find("nd") != None:
            node["node_refs"] = []
            for nd in element.iter("nd"):
                node["node_refs"].append(nd.attrib['ref'])
            
        return node
    
    else:
        return None


#defining the json output file, read from mapfile as file_in parameter
def cleanMyDatabaseAndSaveJsonFile(file_in):
    #step 1 -  cleaning data
    file_out = "OUT.json".format(file_in)
    data = []
    for _, element in ET.iterparse(file_in):
        el = cleanmyfile(element)
        if el:
            data.append(el)
            
    #step 2 -  write to file
    with open(file_out, "w") as f:
        f.write("[\n")
        i = 0
        for item in data:
            i += 1
            if i == 1:
                f.write(json.dumps(item))
            else:
                f.write(",\n" + json.dumps(item))
        f.write("\n]")

    return data


if __name__ == "__main__":

	cleanMyDatabaseAndSaveJsonFile("map.osm")
