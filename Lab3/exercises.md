# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- *edit your response*
	Concrete class. It doesn't have abstract methods and can be instantiated directly.

1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- *edit your response*
	It is a destructor. It is used to define behavior for when an object is garbage collected. It's typically used to ensure resources are cleaned up

1. What class does Texture inherit from?
	- *edit your response*
	Image class

1. What methods and attributes does the Texture class inherit from 'Image'? 
	- *edit your response*
	All the methods and attributes of the Image class

1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- *edit your response*
	It depends on the usage. If a Texture is an Image with some specialized properties, an 'is-a' relationship is better. However, if a Texture uses an image to represent itself, then a 'has-a' relationship would be more better. 

	Code for 'has-a' relationship:
	class Texture(Image):
		def __init__(self, w, h):
			self.image = Image(w, h)

1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- *edit your response*
	Yes, it inherits the constructor of the Image class automatically.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?
*edit the code directly*  
No, if multiple threads attempt to create an instance of the singleton class at the same time, there's a race condition that might result in multiple instances being created. 
  
