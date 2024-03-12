#!/usr/bin/python3
"""Defines a class Square."""

class Square:
	"""Represent a square."""

	def __init__(self, size=0):
		"""Initializes the square.
        	Args:
			self: Variable references the class.
			size: The size of size of the square.
		"""
		if not isinstance(size, int):
			raise TypeError("Size must be an integer")
		elif size < 0:
			raise ValueError("Size must be >= 0")
		self.__size = size
