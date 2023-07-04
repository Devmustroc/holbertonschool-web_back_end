#!/usr/bin/env python3
""" 12. Log stats """

from pymongo import MongoClient

if __name__ == "__main__":
    """ provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://localhost:27017')  # Update MongoDB connection URL if needed
    nginx_logs = client.logs.nginx

    documents = nginx_logs.count_documents({})
    print(f"{documents} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx_logs.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    check = nginx_logs.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{check} status check")

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    print("IPs:")
    for ip in nginx_logs.aggregate(pipeline):
        print(f"\t{ip.get('_id')}: {ip.get('count')}")
