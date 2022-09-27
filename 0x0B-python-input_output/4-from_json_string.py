#!/usr/bin/python3
"""Contains the "from_json_string" function"""

import json


def from_json_string(my_str):
    """Return an object (Python data Structure)
       represented by a JSON string
    """
    data = json.loads(my_str)
    return(data)
