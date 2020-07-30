# Understanding - Write classes for SP/PP that have additional benefits the higher
# tier plan a customer chooses. I believe class inheritance will be effective here if implemented
# with the correct syntax. Ultimately I want to be able to change some Falses to Trues and 
# increase integer for num of devices per plan as well as increasing price string

# Planning - Inherit BP for SP and then Inherit SP for PP. below super() methods 
# assign updated values to respective keys

# Execute -	
# Write the classes for StandardPlan and PremiumPlan here!
# class StandardPlan(BasicPlan):
#     super().__init__(can_stream, can_download, has_SD, has_UHD)
#     num_of_devices = 2
#     has_HD = True
#     price = '$12.99'

# class PremiumPlan(StandardPlan):
#     super().__init__(can_stream, can_download, has_SD, has_HD)
#     num_of_devices = 4
#     has_UHD = True
#     price = '$15.99'

## Above ^ example does not work because super() has no arguments from BasicPlan to inherit.
## Revision:
class StandardPlan:
	can_stream = True
	can_download = True
	num_of_devices = 2
	has_SD = True
	has_HD = True
	has_UHD = False
	price = '$12.99'
class PremiumPlan:
	can_stream = True
	can_download = True
	num_of_devices = 4
	has_SD = True
	has_HD = True
	has_UHD = True
	price = '$15.99'
# Reflect -
# Looking at other solutions, apparently you can still inherit a parent class with above values, you just don't need to use super()
# For example the most DRY result was:
class BasicPlan:
	can_stream = True
	can_download = True
	num_of_devices = 1
	has_SD = True
	has_HD = False
	has_UHD = False
	price = '$8.99'
	
class StandardPlan(BasicPlan):
	num_of_devices = 2
	has_HD = True
	price = '$12.99'
	
class PremiumPlan(StandardPlan):
	num_of_devices = 4
	has_UHD = True
	price = '$15.99'


# Understanding:
# Create a method that returns a f'string' on how a person's age compares to someone else's
# name/age is initialized, how can i implement logic between ages
# reference rock/paper/scissors for basic logic comparisons between 2 values

# Planning:
# if self.age > other.age:
# return f'other is younger than me'
# elif self.age < other.age:
# return f'other is older than me'
# else:
# return f'other is the same age as me'
# Execute:
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def compare_age(self, other):
		if self.age > other.age:
			return f'{other.name} is younger than {self.name}'
		elif self.age < other.age:
			return f'{other.name} is older than {self.name}'
		else:
			return f'{other.name} is the same age as {self.name}'
# Reflect/Refactor:
# Top voted most DRY returned other.name + ' is older than me'
# SO CLOSE THE LOGIC CHECKED OUT
# Next time be mindful of explicit directions.
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def compare_age(self, other):
		if other.age > self.age:
			return other.name + ' is older than me.'
		elif other.age < self.age:
			return other.name + ' is younger than me.'
		else:
			return other.name + ' is the same age as me.'
# If answer looks the same but fails ALWAYS TRIPLE CHECK casing/spelling/punctuation


# Understand:
# Create constructor for circles. Includes getArea method and getPerimeter method.
# Formulas provided for both i.e Plr^2 and 2Pl*r
# Examine Rectangle
# Plan:
# Examine
# Execute:

# Reflect/Refactor:
#