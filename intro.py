

print("Hello World from python!")
print(2)
print(7+3)
print(True)

# this is a comment
""" 
Multiple
Line
Comment
"""

#Creating Variables
name = "Zane"
age = 32
last_name = "Moon"
found = False
another_age = "50"
pets = True

print(name)
print(last_name)

#Concatenation
#Casting => convert a data type to another one(e.g. string (str) -> numbers (int))
#or numbers (int) -> string (str)
concatenation_example = "My name is: " + name + " " + last_name + " and I'm learnig about python! I am " + str(age) + " years old!"
print("My name is: " + name + " " + last_name + " and I'm learning about python! I am " + str(age) + " years old!")
print("Did he show up to class? " + str(found))
print(100 + int(another_age))
print(concatenation_example)

#The f format
#f"" or f""""""
print(f"My name is: {name}, and I'm {age} years old!")
print(f"""
My name is {name}
    and this is an example
of a triple double quote f format
    """)

#the type() function helps us to know the data type of the variables
print(type(name))
print(type(found))
print(type(age))

#Casting
#Helps us to conver different data typs
#str() -> convert any data type to string
#int() -> convert string number to Numeric values
#float() -> convert string number to float type

#Input Function/Method
#is going to allow us to interact with the terminal and pass some values
#input()
#print(input("Enter your name here:"))
#print(type(input("Enter your age here:")))
#new_age = int(input("Enter new age:"))
#print(new_age + age)

x = int(input("Enter a first value: "))
y = int(input("Enter a second value: "))
print(x+y)