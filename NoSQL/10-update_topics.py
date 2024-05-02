#!/usr/bin/env python3
"""change all topics of a school document based on the name"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Python function that changes all topics of
    a school document based on the name"""
    myquery = {"name": name}
    newvalues = {"$set": {"topics": topics}}

    mongo_collection.update_one(myquery, newvalues)
