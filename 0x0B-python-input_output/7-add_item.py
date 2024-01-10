#!/usr/bin/python3
"""
A script that add all arguments to a python list, and save them to a file.
"""

import sys
import json
save_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file
try:
    data = load_from_json('add_item.json')
except (ValueError, FileNotFoundError):
    data = []

data.extend(sys.argv[1:])
save_file(data, 'add_item.json')
