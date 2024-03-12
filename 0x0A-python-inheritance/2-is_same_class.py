#!usr/bin/python3
"""A function which checks whether the object is an instance of the specified class."""

def is_same_class(obj, a_class):
	""" Checks if the object is an instance of the specified class.

	Args:
		obj: Object to check.
		a_class: The class to match the object.
	Returns:
		True if the object is the exact instance of the determined class; else False.
	"""
	if type(obj) == a_class:
		return (True)
	return (False)
