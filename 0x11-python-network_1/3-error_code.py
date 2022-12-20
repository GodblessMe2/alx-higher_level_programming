#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    res = urllib.request
    request = res.Request(url)
    try:
       with res.urlopen(request) as response:
          print(dict(response.headers).get("X-Request-Id"))
    except res.error.HTTPError as e:
       print("Error code: {}".format(e.code))
