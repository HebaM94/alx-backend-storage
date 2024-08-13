#!/usr/bin/env python3
"""PyMongo operations"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    Return: new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
