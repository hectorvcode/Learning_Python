'''
Exercise: Level 1
Check the python version you are using

personal@DESKTOP-GN68TNB MINGW64 /c/dev/python (main)
$ python --version
Python 3.14.3
'''


'''
Open the python interactive shell and do the following operations. The operands are 3 and 4.
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//)
'''
print("addition", 3 + 4)
print("substraction", 3 - 4)
print("multiplication", 3 * 4)
print("division", 3 / 4)
print("modulus", 3 % 4)
print("exponential", 3 ** 4)
print("floor division", 3 // 4)



'''
Write strings on the python interactive shell. The strings are the following:
Your name
Your family name
Your country
I am enjoying 30 days of python
'''
print("Hector")
print("Vasquez")
print("Colombia")
print("I am enjoying 30 days of python")



'''
Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country
'''
print("type of 10", type(10))
print("type of 9.8", type(9.8))
print("type of 3.14", type(3.14))
print("type of 4 - 4j", type(4 - 4j))
print("type of ['Asabeneh', 'Python', 'Finland']", type(['Asabeneh', 'Python', 'Finland']))
print("type of Hector", type("Hector"))
print("type of Vasquez", type("Vasquez"))
print("type of Colombia", type("Colombia"))

'''
1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
'''
print("Integer - 46", type(46))
print("Float - 3.75", type(3.75))
print("Complex - 2 + 5j", type(2 + 5j))
print("String - This is a string", type("This is a string"))
print("Boolean - True", type(True))
print("List - ['Hector', 'Natalia', 'Alison', 'Danna']", type(['Hector', 'Natalia', 'Alison', 'Danna']))
print("Tuple - ('Mario', 'Luider', 'Vanesa')", type(('Mario', 'Luider', 'Vanesa')))
print("Set - {0,1,2,3}", type({0,1,2,3}))
contacto = {
    "pais":"Colombia",
    "ciudad":"Bogota",
    "localidad":"Engativa",
    "barrio":"La Estradita"
}
print("Dictionary - contacto", type(contacto))

'''
2. Find an Euclidean distance between (2, 3) and (10, 8)
'''
x2 = 2
x1 = 10
y2 = 3
y1 = 8
euclidean_distance = ((x2-x1)**2 + (y2-y1)**2) ** (1/2)
print(euclidean_distance)