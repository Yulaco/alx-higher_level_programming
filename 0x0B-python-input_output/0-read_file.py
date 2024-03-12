#!/usr/bin/python3

"""Defines read function for text file (UTF8)."""

def read_file(filename=""):
	"""Prints information of text file (UTF8) to stdout."""
	with open(filename, encoding="utf-8") as f:
		print(f.read(), end="")
