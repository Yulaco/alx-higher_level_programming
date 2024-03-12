*Python - Inheritance*

*0. Lookup*

	- A function that returns the list of available attributes and methods of an object.
	- Prototype: def lookup(obj):

*1. My list*

	- A class MyList that inherits from list.
	- Public instance method: def print_sorted(self):

*2. Exact same object*

	- A function that returns True if the object is exactly an instance of the specified class ; otherwise False.
	- Prototype: def is_same_class(obj, a_class):

*3. Same class or inherit from*

	- A function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
	- Prototype: def is_kind_of_class(obj, a_class):

*4. Only sub class of*

	- A function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
	- Prototype: def inherits_from(obj, a_class):

*5.  Geometry module*

	- An empty class BaseGeometry.

*6. An empty class BaseGeometry.*

	- A class BaseGeometry (based on 5-base_geometry.py).
	- Public instance method: def area(self):

*7. Integer validator*

	- A class BaseGeometry (based on 6-base_geometry.py).
	- Public instance method: def area(self):

*8. Rectangle*

	- A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
	- Instantiation with width and height: def __init__(self, width, height):

*9. Full rectangle*

	- A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
	- Instantiation with width and height: def __init__(self, width, height):

*10. Square #1*

	- A class Square that inherits from Rectangle (9-rectangle.py).
	- Instantiation with size: def __init__(self, size):

*11. Square #2*

	- A class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
	- Instantiation with size: def __init__(self, size):
