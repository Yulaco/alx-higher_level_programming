#!/usr/bin/python3

"""Function which defines a class and inhereted class."""

def is_kind_of_class(obj, a_class):
	"""Check if an object is an instance or an instance of a class.

	Args:
		obj: object to check.
		a_class: Class to match the type of object.
	Returns:
		True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.		"""
	if isinstance(obj, a_class):
		return (True)
	else:
		return (False)
