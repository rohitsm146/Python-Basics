'''x = 42
print(f"Type:     {type(x)}")
print(f"Value:    {x}")
print(f"Identity: {id(x)}")'''

'''a = 256
b = 256
print(f"a is b: {a is b}")    # True — cached'''

"""c = 257
d = int(input("Enter a number: "))
print(f"c is d: {c is d}")  
"""
name = "Python"
greeting = name
print(f"id(name)     = {id(name)}")
print(f"id(greeting) = {id(greeting)}")

name = "C"
print(f"id(name)     = {id(name)}")
print(f"id(greeting) = {id(greeting)}")
print(f"greeting     = {greeting}")
