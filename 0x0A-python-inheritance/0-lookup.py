#!/usr/bin/ptyhon3
""" Define an object's attribute lookup function."""

def lookup(obj):
	"""Returns the list of available attribute and the object."""
	return (dir(obj))
