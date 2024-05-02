#!/usr/bin/env python3

"""Python function that inserts a new document
in a collection based on kwargs"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """Insert a document into the mongo collection"""
    dbresult = mongo_collection.insert(kwargs)
    return dbresult.inserted_id
