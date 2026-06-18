'''
Exercises Level 1
'''
# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2: 30 Days of python programming

# Declare a first name variable and assign a value to it
name = 'Hector'

# Declare a last name variable and assign a value to it
last_name = 'Vasquez'

# Declare a full name variable and assign a value to it
full_name = name + " " +  last_name
full_name = f'{name} {last_name}'
print(full_name)

# Declare a country variable and assign a value to it
country = 'Colombia'

# Declare a city variable and assign a value to it
city = 'Bogota'

# Declare an age variable and assign a value to it
age = 25

# Declare a year variable and assign a value to it
year = 2006

# Declare a variable is_married and assign a value to it
is_married = True

# Declare a variable is_true and assign a value to it
is_true = True

# Declare a variable is_light_on and assign a value to it
is_light_on = True

# Declare multiple variable on one line
pet_name, pet_age, is_adopted = "Chispita", 5, True


'''
Exercises Level 2
'''
# Check the data type of all your variables using type() built-in function
for var_name, var_value in {'name':name, 'last_name':last_name, 'full_name':full_name, 'country':country, 'city':city, 'age':age, 'year':year, 'is_married':is_married, 'is_true':is_true, 'is_light_on':is_light_on}.items():
    print(var_name, '->', type(var_value))

# Using the len() built-in function, find the length of your first name
first_name = 'Hector'
print(len(first_name))

# Compare the length of your first name and your last name
first_name = 'Hector'
last_name = 'Vasquez'
len(first_name)
len(last_name)

if len(first_name) == len(last_name):
    print('Tienen la misma longitud')
elif len(first_name) > len(last_name):
    print('El nombre es más largo')
else: 
    print('El apellido es mas largo')

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# The radius of a circle is 30 meters.
import math
radius = 30

# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area = math.pi * radius ** 2

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circumference = math.pi * 2 * radius

# Take radius as user input and calculate the area.
import math
radius = float(input('Enter the radius value'))
area =  math.pi * radius ** 2

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('Enter your first name')
last_name = input('Enter your last name')
country = input('Enter your country')
age = int(input('How old are you?'))

# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
