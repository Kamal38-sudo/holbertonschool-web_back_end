#!/usr/bin/env python3
"""
10-update_topics.py
Module that updates the topics of a school document based on the name
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the school name

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object
        name (str): The school name to update
        topics (list of str): List of topics to set in the document
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
