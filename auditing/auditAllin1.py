import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
import sys

OSMFILE = "map.osm"

def audit(osmfile,argumentToPass):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
		if elem.tag == "node":
			
			if argumentToPass == "building":
				for tag in elem.iter("tag"):
					if tag.attrib['k'] == "building":
						print tag.tag, tag.attrib
            
			if argumentToPass == "email":
				for tag in elem.iter("tag"):
					if tag.attrib['k'] == "email":
						print tag.tag, tag.attrib
			
			if argumentToPass == "postcode":
				for tag in elem.iter("tag"):
					if tag.attrib['k'] == "addr:postcode":
						print tag.tag, tag.attrib
			
			if argumentToPass == "source":
				for tag in elem.iter("tag"):
					if tag.attrib['k'] == "source":
						print tag.tag, tag.attrib

			if argumentToPass == "city":
				for tag in elem.iter("tag"):
					if tag.attrib['k'] == "addr:city":
						print tag.tag, tag.attrib						

def test(argumentToPass):	
	audit(OSMFILE,argumentToPass)
   
 


if __name__ == '__main__':
	argumentToPass = sys.argv[1]
	print ""+argumentToPass
	test(argumentToPass)