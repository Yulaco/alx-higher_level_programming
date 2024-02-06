#!/usr/bin/python3

"""Defines append function which writes a string at the end of a text file."""

def append_write(filename="", text=""):
	"""Appends string in text file (UTF8)."""

	with open(filename, 'a', encoding="utf-8") as f:
		return(f.write(text))
