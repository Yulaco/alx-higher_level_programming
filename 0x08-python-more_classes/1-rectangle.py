#!/usr/bin/python3
"""Module defines a class rectangle."""

class Rectangle:
	"""Represents a rectangle."""

	def __init__(self, width=0, height=0):
		"""Rectangle initialization.

		Args:
			width (int): Width of rectangle.
			height (int): Height of rectangle.
		"""
		self.width = width
		self.height = height

	@property
	def width(self):
		"""Retrieve private instance attribute for width."""
		return self.__width

	@width.setter
	def width(self, value):
		"""Setter for the private instance attribute width."""
		if type(value) is not int:
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	@property
	def height(self):
		"""Retrieve private instance attribute for height."""
		return self.__height

	@height.setter
	def height(self, value):
		"""Setter for the private instance attribute height."""
		if type(value) is not int:
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value
