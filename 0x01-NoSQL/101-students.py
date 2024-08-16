#!/usr/bin/env python3
""" Aggregation operations """
from collections import OrderedDict


def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    pipeline = [{'$addFields': {'averageScore': {'$avg': '$topics.score'}}},
                {'$sort': OrderedDict([('averageScore', -1), ('name', 1)])}]
    return mongo_collection.aggregate(pipeline)
