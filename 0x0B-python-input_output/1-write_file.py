#!/usr/bin/python3

"""Defines function that writes to text file (UTF8)."""

def write_file(filename="", text=""):	
	"""Returns number of characters written."""

	with open(filename, "w", encoding="utf-8") as f:
		return(f.write(text))
