#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs using MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    """ provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f'{total_logs} logs')

    print('Methods:')
    for x in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = collection.count_documents({"method": x})
        print(f'\tmethod {x}: {method_count}')

    check_get = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{check_get} status check")
