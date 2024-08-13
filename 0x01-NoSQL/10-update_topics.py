#!/usr/bin/env python3
"""PyMongo operations"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    """
    return mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
