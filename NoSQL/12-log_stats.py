#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient, DESCENDING

if __name__ == "__main__":

    client = MongoClient('mongodb://127.0.0.1:27017')
    ngnix_log = client.logs.nginx

    documents = ngnix_log.count_documents({})
    print("{} logs".format(documents))

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(
            method,
            ngnix_log.count_documents({"method": method})
        ))

    print("{} status check".format(
        ngnix_log.count_documents({"$and": [{"path": "/status"},
                                                   {"method": "GET"}]})
    ))

    pipeline = [
            {
                "$group": {
                    "_id": "$ip",
                    "count": {"$sum": 1}
                }
            },
            {
                "$sort": {
                    "count": DESCENDING
                }
            },
            {
                "$limit": 10
            }
        ]

    print("IPs:")
    res = list(ngnix_log.aggregate(pipeline))
    for item in res:
        print("\t{}: {}".format(item.get("_id"), item.get("count")))