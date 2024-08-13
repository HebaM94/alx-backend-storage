#!/usr/bin/env python3
"""
Aggregation operations
"""
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")


db = client.logs
nginx_collection = db.nginx


total_logs = nginx_collection.count_documents({})


print(f"{total_logs} logs")


print("Methods:")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

for method in methods:
    method_count = nginx_collection.count_documents({"method": method})
    print(f"\tmethod {method}: {method_count}")

status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})

print(f"{status_check_count} status check")
