#!/usr/bin/python3

"""Defines create an object JSON file funtion."""

import json

def load_from_json_file(filename):
	"""Creates JSON file."""
	with open(filename, "r", encoding="utf-8") as f:
		return(json.load(f))
