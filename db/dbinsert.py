#!/usr/bin/env python

import json
import sys
from pymongo import MongoClient
#conversion of osm to json
def insert_data(data, db):
    db.OpenStreetMap.cracow.insert(data)

if __name__ == "__main__":
	client = MongoClient("mongodb://localhost:27017")
	db = client.examples
	filename = "OUT.json"
	with open(filename) as f:
		data = json.loads(f.read())
		insert_data(data, db)
