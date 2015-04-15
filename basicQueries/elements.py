#!/usr/bin/env python

import pprint
import sys
    
def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db



def aggregate(db, pipeline):
    result = db.OpenStreetMap.cracow.aggregate(pipeline)
    return result

if __name__ == '__main__':

#objective is to gather some statistics about elements   
        
    db = get_db('examples')
pipeline = [ { "$group" : {"_id" : "$type", 
                                   "count" : { "$sum" : 1 } 
                                   } },                
                     { "$sort" : { "count" : -1}}]




result = aggregate(db, pipeline)

pprint.pprint(result["result"])