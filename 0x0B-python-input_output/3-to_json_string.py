#!/usr/bin/python3
"""
Contains the "to_json_string" function
"""

import json


def to_json_string(my_obj):
    """Return the JSON representative of an object(string)"""
    json_str = json.dumps(my_obj)
    return(json_str)
