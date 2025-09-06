# Arithmetic
# Assignment
# Comparison
# Logical
# Identity
# Membership

# Arithmetic operator - used with numeric values to perform common math

x = 1
y = 2
res = 0

res = x + y
print(res)

res = x - y
print(res)

res = x / y
print(res)

res = x % y
print(res)

res = x ** y
print(res)

res = x // y
print(res)

print("-----------------------")

# Assignment operators - used to assing values to variables

x = 5
x += 5
x -= 3
x *= 3
x /= 3
print(x)
print("-----------------------")

# Comparison operators - used to compare two values
# if_else statements

# Logical operators - used to combine conditional statements

x = 3
y = 2
z = 2

print(x == y and y == z) # Both conditions need to be true
print(x == y or y == z) # Only one conditions needs to be true
print(not x == y)
print("-----------------------")

# Identity operators - used to compare the objects, not if they're equal but if they're actually the same object with the same memory location

x = 3
y = 3
print(x is y) # True if both variables are the same object
print(x is not y) 
print("-----------------------")

# Membership operator - used to test if a sequence is presnted in an object

x = [1, 2, 3, 4, 5] # this is a list

print(3 in x)
print(9 not in x)
print("-----------------------")
