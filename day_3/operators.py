'''
Operators
Python language supports several types of operators 
'''


'''
Assignment Operators
They're used to assign values to variables 
Let us take = as an example
The Equal sign in Python it means we are storing a value in a certain variable
we call it assignment or assigning value to a variable
Please review the image on the day_3 folder
'''

'''
Arithmetic Operators
Addition(+): a + b
Subtraction(-): a - b
Multiplication(*): a * b
Division(/): a / b
Modulus(%): a % b
Floor division(//): a // b
Exponentiation(**): a ** b
'''


# Integers
print("Addition", 1 + 2)
print("Subtraction", 2 - 1)
print("Multiplication", 2 * 3)
print("Division1", 4 / 2)
print("Division2", 6 / 2)
print("Division3", 7 / 2)
print("Division without the remainder1", 7 // 2)
print("Division without the remainder2", 7 // 3)
print("Modulus", 3 % 2)
print("Exponentiation", 2 ** 3)


# Floats
print('Floating Point Number PI', 3.1416)
print('Floating Point Number gravity', 9.81)


# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ', (1 + 1j) * (1 - 1j))


# Example
a = 3
b = 2

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total)
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)


# Calculating area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print('Area of a circle: ', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle: ', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

# Calculate the density of a liquid
mass = 75
volume = 0.075
density = mass / volume
print(density, 'Kg/m^3')


'''
Comparison Operators

In programming we compare values, we use comparison operatos to compare two values. We check if a value is greater or less or equal to other value
Please check the table in the folder
'''
print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 < 3)
print(2 <= 3)
print(3 == 2)
print(3 != 2)
print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
print(len('mango') < len('avocado'))
print(len('milk') != len('meat'))
print(len('milk') == len('meat'))
print(len('tomato') == len('potato'))
print(len('python') > len('dragon'))

# Comparing something gives either a True or False
print('True == True: ', True == True)
print('True == false: ', True == False)
print('False == False: ', False == False)


'''
In addition to the above comparison operator Python uses:
* is: returns true if both variables are the same object(x is y)
* is not: returns true if both variables are not the same object (x is not y)
* in: returns true if the queried list contains a certain item (x in y)
* not in: returns true if the queried list doesn't have a certain item (x not in y)
'''

print('1 is 1: ', 1 is 1)
print('1 is not 2: ', 1 is not 2)
print('A in Asabeneh: ', 'A' in 'Asabeneh')
print('B not in Asabeneh: ', 'B' not in 'Asabeneh')
print('coding' in 'coding for all')
print('a in an: ', 'a' in 'an')
print('4 is 2 ** 2: ', 4 is 2 ** 2)


'''
Logical Operators

Unlike other programming languages python uses keyworkds and, or and not for logical operators.
logical operators are used to bombine conditional statements
Please check the image operators_logical

and     returns True if both statements are true
or      returns True if one of the statements is true
not     reverse the result, returns False if the result is true
'''
# Examples
print(3 > 2 and 4 > 3)
print(3 > 2 and 4 < 3)
print(3 < 2 and 4 < 3)
print('True and True: ', True and True)

print(3 > 2 or 4 > 3)
print(3 > 2 or 4 < 3)
print(3 < 2 or 4 < 3)
print('True or False: ', True or False)

print(not 3 > 2)
print(not True)
print(not False)
print(not not True)
print(not not False)