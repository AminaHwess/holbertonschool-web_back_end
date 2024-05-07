#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs using MongoDB"""

from pymongo import MongoClient

# Importing the list_all function from the 8-all module
list_all = __import__("8-all").list_all

if __name__ == "__main__":
    # Connecting to the MongoDB client
    client = MongoClient("mongodb://127.0.0.1:27017")

    # Accessing the nginx collection within the logs database
    ngix_collection = client.logs.nginx

    # Counting the total number of logs in the nginx collection
    logs = ngix_collection.count_documents({})

    # Printing the total number of logs
    print("{} logs".format(logs))

    # Defining a list of HTTP methods to iterate over
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # Printing the available methods
    print("Methods:")

    # Iterating over the HTTP methods and printing the count for each
    for method in methods:
        count = ngix_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Counting the number of GET requests to the /status path
    count = ngix_collection.count_documents({"method": "GET",
                                            "path": "/status"})

    # Printing the number of status checks
    print(f"{count} status check")
