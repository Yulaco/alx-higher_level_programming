#!/usr/bin/python3

"""Defines JSON object(string) function."""

import json

def to_json_string(my_obj):
	"""Returns json representation of a string."""
	return(json.dumps(my_obj))
