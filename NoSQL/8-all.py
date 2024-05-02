#!/usr/bin/env python3

"""function that lists all documents in a collection"""


import pymongo


def list_all(mongo_collection):
    """list all documents in a collection"""

    mydocs = mongo_collection.find()

    if mongo_collection.count_documents({}) == 0:
        return []
    else:
        return mydocs
