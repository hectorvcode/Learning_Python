'''
We have lots of built-in functions
They're globally available for your use without imporitng or configuring
Somo of the most commonly used are:
print()
len()
type()
int()
float()
str()
input()
list()
dict()
min()
max()
sum()
sorted()
open()
file()
help()
dir()
'''

print("Hello World!")
print(len("Hector"))
print(type("Vasquez"))
print(str(10))
print(type(str(19)))
print(int("10"))
print(float(10))
nombre = input("Enter your name:")
print("El nombre es: ",nombre)


'''
There is a list of te Python keywords

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                
'''
help('keywords')



'''
There is information about string

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to 'utf-8'.
 |  errors defaults to 'strict'.
 |                                                                                                                                                                                                                  
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.                                                                                                                                       
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getitem__(self, key, /)
 |      Return self[key].            
'''
help(str)

# gives the minimum value
print("min", min(20, 30, 40, 50))

# gives the maximum value
print("max", max(20, 30, 40, 50))

# it takes list as an argument and return min
print("list min", min([10, 20, 30, 40, 50, 60]))

# it takes list as an argument and return max
print("list max", max([10, 20, 30, 40, 50, 60]))

# it takes list as an argument and return the sum 
print("list sum", sum([10, 20, 30, 40, 50, 60]))