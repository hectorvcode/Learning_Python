# Declare your age as integer variable
age = 46

# Declare your height as a float variable
height = 1.77

# Declare a variable that store a complex number
complex_number = 1 + 2j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base  = input('Enter base: ')
height = input('Enter height: ')
area = 0.5 * float(base) * float(height)
print('The area of the triangle is ', area)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
perimeter = float(side_a) + float(side_b) + float(side_c)
print('The perimeter of the triangle is: ', perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
lenght = float (input('Enter the lenght: '))
width = float (input('Enter the width: '))
area =  lenght * width
perimeter = 2 * (lenght + width)
print(f'The area of the rectangle is {area} and the perimeter is {perimeter}')

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
import math
radius = float(input('Enter the radius of the circle: '))
area = math.pi * radius * radius 
circumference = 2 * math.pi * radius
print(f'The area of the circle is {area} and the circumference is {circumference}')

# Calculate the slope, x-intercept and y-intercept of y = 2x -2


# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# There is no 'on' in both dragon and python
# Find the length of the text python and convert the value to float and convert it to string
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# Check if type of '10' is equal to type of 10
# Check if int('9.8') is equal to 10