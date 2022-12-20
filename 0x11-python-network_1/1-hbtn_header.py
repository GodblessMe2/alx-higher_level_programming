#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    res = urllib.request
    request = res.Request(url)
    with res.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
