*Python - Input/Output*

*0. Read file*

	- A function that reads a text file (UTF8) and prints it to stdout.
	- Prototype: def read_file(filename=""):

*1. Write to a file*

	- A function that writes a string to a text file (UTF8) and returns the number of characters written.
	- Prototype: def write_file(filename="", text=""):

*2. Append to a file*

	- A function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
	- Prototype: def append_write(filename="", text=""):

*3. To JSON string*

	- A function that returns the JSON representation of an object (string).
	- Prototype: def to_json_string(my_obj):

*4. From JSON string to Object*

	- A function that returns an object (Python data structure) represented by a JSON string.
	- Prototype: def from_json_string(my_str):

*5 Save Object to a file*

	- A function that writes an Object to a text file, using a JSON representation.
	- Prototype: def save_to_json_file(my_obj, filename):

*6. Create object from a JSON file*

	- A function that creates an Object from a "JSON file".
	- Prototype: def load_from_json_file(filename):

*7. Load, add, save*

	- A script that adds all arguments to a Python list, and then save them to a file.

*8. Class to JSON*

	- A function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.
	- Prototype: def class_to_json(obj):

*9. Student to JSON*

	- A class Student that defines a student.
	- Public method def to_json(self):

*10. Student to JSON with filter*

	- A class Student that defines a student.
	- Public method def to_json(self, attrs=None):

*11. Student to disk and reload*

	- A class Student that defines a student by: (based on 10-student.py).
	- Public method def reload_from_json(self, json):

*12. Pascal's Triangle*

	- Create a function def pascal_triangle(n):
