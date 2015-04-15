#!/usr/bin/env python

import pprint
	
def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
#objective is to count iddividual users
    pipeline = [  
                 { "$group" : {"_id" : "$created.user",			 
                               "count" : { "$sum" : 1 }}},
                 { "$group" : {"_id" : "$user",			 
                               "count" : { "$sum" : 1 }}},              
                 { "$sort" : { "count" : -1}} 
                  ]
    return pipeline

def aggregate(db, pipeline):
    result = db.OpenStreetMap.newdelhi.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    pprint.pprint(result["result"])