#!/usr/bin/python3

"""Define class MyList that inherits from list."""

class MyList(list):
	"""Implement sorted printing for the list class."""

	def print_sorted(self):
		"""Print sorted list in ascending order."""
		print(sorted(self))
