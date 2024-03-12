#!/usr/bin/python3
"""Defines a class Square."""

class Square:
	"""Defines properties of a square."""

	def __init__(self, size=0):
		"""Initialize a square.
		Args:
			self: Variable references the class.
			size: The sizeof the square.
		"""
		if not isinstance(size, int):
			raise TypeError("Size must be an integer")
		elif size < 0:
			raise ValueError("Size must be >= 0")
		self.__size = size

	def area(self):
		"""
		Args:
			self: Variable referring to Square.
		Returns:
			Returns the current square area.
		"""
		return (self.__size * self.__size)
