#!/usr/bin/env python3
"""PyMongo operations"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    Return: empty list if no document in the collection
    """
    return mongo_collection.find()
