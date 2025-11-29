#!/usr/bin/env python3
"""
11-schools_by_topic.py
Module that returns the list of schools having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns all schools having a specific topic in their 'topics' list

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection object
        topic (str): The topic to search for

    Returns:
        list: List of school documents matching the topic
    """

    return list(mongo_collection.find({'topics': topic}))
