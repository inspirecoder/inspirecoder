# Constructors are generally used for instantiating an object. 
class Multiplication:
    # The task of constructors is to initialize (assign values)
    # to the data members of the class when an object of the class is created.
	first_value = 0
	second_value = 2
	answer = 0
	
 # In Python the __init__() method is called the constructor and is always called 
 # when an object is created.
 # The `__init__` method lets the class initialize the object's attributes
 # and serves no other purpose. It is only used within classes.
 
 # parameterized constructor - 
 # constructor with parameters is known as parameterized constructor. 
 # The parameterized constructor takes its first argument as a reference
 # to the instance being constructed known as self 
 # and the rest of the arguments are provided by the programmer.
 
	def __init__(self, fv, sv):
		self.first_value = fv
		self.second_value = sv
	
	def display(self):
		#print("First number = " + int(self.first_value))
		#print("Second number = " + int(self.second_value)) 
        ##  msg for these above statements: can only concatenate str (not "int") to str
        print("First number = " + str(self.first_value))
		print("Second number = " + str(self.second_value)) 
		print("Addition of two numbers = " + int(self.answer))

	def calculate(self):
		self.answer = self.first_value + self.second_value

# creating object of the class
# this will invoke parameterized constructor

# The task of constructors is to initialize (assign values) 
# to the data members of the class when an object of the class is created.

# when we execute obj = Multiplication() , Python gets to know that 
# obj is an object of class Multiplication and calls the constructor of that class to create an object.
obj = Multiplication(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()
