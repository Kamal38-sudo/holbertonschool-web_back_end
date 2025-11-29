#!/usr/bin/env python3
"""
9-insert_school.py
Module that inserts a new document in a MongoDB collection
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object
        **kwargs: Key-value pairs to insert as a document

    Returns:
        ObjectId: The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
