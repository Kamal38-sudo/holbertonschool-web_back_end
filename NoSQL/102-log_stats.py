#!/usr/bin/python3
"""
Script that provides some stats about Nginx logs stored in MongoDB:
- Total number of logs
- Number of logs by method (GET, POST, PUT, PATCH, DELETE)
- Number of logs with method=GET and path=/status
- Top 10 most frequent IPs
"""

from pymongo import MongoClient

def main():
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count by method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count of status check
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

    # Top 10 IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 10}
    ]
    top_ips = collection.aggregate(pipeline)
    print("IPs:")
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    main()
