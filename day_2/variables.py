'''
Variables store data in a computer memory
Mnemonic variables are recommended to use. A mnemonic variable is a variable name that can be easily remembered and associated
A variable refers to a memory address in which data is stored
When naming a variable is not allowed: number at the begining, special character, hyphen
A variable can have a short name, ie. x, y, z but it's recommended a more descriptive name like firstname, lastname, age, country, etc
'''

'''
Python variable name rules

* A variable name must start with a letter or the underscore character
* A variable name cannot start with a number
* A variable name can only contain: alpha-numeric characters and underscores 
* Variable names are case-sensitive: firstname, Firstname, FirstName, FIRSTNAME are different variables
'''

'''
Invalid variable names

first-name
first@name
first$name
num-1
1num
'''


'''
Python developers use snake case variable naming convention (snake_case)
We use underscore character after each word for a variable containing more than one word, ie. first_name, engine_rotation_speed
The equal sign is an assignment operator, ie. firstname = "Hector"
'''

# Variables in Python
first_name = 'Hector'
last_name = 'Vasquea'
country = 'Colombia'
city = 'Bogota'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Hector',
   'lastname':'Vasquez',
   'country':'Colombia',
   'city':'Bogota'
   }


'''
Print function takes unlimited number of arguments. An argument is a value which can be passed or put inside the function parenthesis 
'''
print("Hello World!") # The text inside the parenthesis is an argument
print("a", "b", "c", "d") # It can take multiple arguments
print(len("Hector")) # It takes only one argument



'''
Declaring Multiple Variable in a Line
'''
first_name, last_name, country, age, is_married = "Hector", "Vasquez", "Colombia", 46, True
print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)



'''
Getting user input
'''
first_name = input("Write your name: ")
age = input("How old are you?: ")

print(first_name)
print(age)


'''
Checking Data types and Casting
Different python data types
Let's declare variables with various data types
'''
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city= 'Helsinki'
age = 250



'''
Printing out types
'''
print(type('Asabeneh'))                 
print(type(first_name))          
print(type(10))                  
print(type(3.14))                
print(type(1 + 1j))              
print(type(True))                
print(type([1, 2, 3, 4]))        
print(type({'name':'Asabeneh'})) 
print(type((1,2)))               
print(type(zip([1,2],[3,4])))    


'''
Casting 
Converting one data type to another data time
We use int(), float(), str(), list, set
If we contatenate a number with a string the number should be first converted to a string
'''

# int to float
num_int = 10
print("num_int", num_int)
num_float = float(num_int)
print("num_float", num_float)

# float to int
gravity = 9.81
print(int(gravity))

# int to str
num_int= 10
print(num_int)
num_str = str(num_int)
print(num_str)

# str to int or float
num_str = "10.6"
num_float = float(num_str)
num_int = int(num_float)
print("num_int", int(num_int))
print("num_float", float(num_str))
num_int = int(num_float)
print("num_int", int(num_int))

# str to list
first_name = "Asabeneh"
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)


'''
Numbers

* Integers (negative, zero and positive). i.e.: -3, -2, -1, 0, 1, 2, 3
* Floating Point Numbers (decimal numbers). i.e.: -3.5, -2.25, 0.0, 1.2, 3.5
* Complex Numbers. i.e.: 1 + j, 2 + 4j, 1 - 1j

'''