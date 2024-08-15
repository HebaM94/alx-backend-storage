#!/usr/bin/env python3
""" Redis Basics """
import redis
import requests
from functools import wraps
from typing import Callable


client = redis.Redis()


def track_get_page(fn: Callable) -> Callable:
    """ Decorator for get_page """
    @wraps(fn)
    def wrapper(url: str) -> str:
        """ Wrapper that:
            - check whether a url's data is cached
            - tracks how many times get_page is called
        """
        client.incr(f'count:{url}')
        cached_page = client.get(f'result:{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        client.set(f'result:{url}', response, ex=10)
        return response
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """ Makes a http request to obtain the HTML content of
        a particular URL and returns it"""
    response = requests.get(url)
    return response.text
