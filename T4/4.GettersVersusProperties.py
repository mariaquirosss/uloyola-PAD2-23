class Student:
	
	def __init__(self,name:str):
		self.__name = name

	# Getter of the attribute
	def get_name(self):
		return self.__name

	# Similar as Getter (get value of an attribute)
	@property 
	def name(self):
		return self.__name

	# Setter of the attribute
	def set_name(self, newname:str):
		self.__name = newname

	# Simiar as Setter (set value of an attibute)
	@name.setter 
	def name(self,newname: str):
		self.__name = newname

## EXAMPLES ##

# Set the value using the Constructor
std = Student("Pedro") 

# Get the value using Getter
print(f"Using Getter: ",std.get_name()) 

# Get the value using @property
print(f"Using @property: ",std.name)  #'Pedro' .


# Set the value using Setter.
std.set_name("Matilde1")

# Get the value using @property Getter.
print(f"Value updated using Setter method: ",std.name)  #'Matilde1' 

# Set the value using @property.Setter
std.name = 'Matilde2'

# Get the value using @property Getter.
print(f"Value update using property: ",std.name)  #'Matilde2'


# Error trying to access directly to the the private attribute
print(std.__name) #'Matilde' 