#!/usr/bin/python3
"""a module that returns an object rep by json string"""
import json

def from_json_string(my_str):
    """ a function that returns object rep by JSON string"""
    return json.loads(my_str)
