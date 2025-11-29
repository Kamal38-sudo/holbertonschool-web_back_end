//  List all documents in Python
#!/usr/bin/env python3
""" 8-all.py """

def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        list of documents, or empty list if none
    """
    if mongo_collection is None:
        return []

    # find() returns a cursor, convert to list
    documents = list(mongo_collection.find())
    return documents

