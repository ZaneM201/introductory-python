# Simple function
def my_function():
    print("This is my Function")

def other_function():
    print("This is another function")

my_function() # calling the function
other_function()

print("-----------------------")

# Function with perameters
def print_full_name(fname, last_name):
    print("This name is: {fname} {last_name}")

# Function that returns something
def get_full_name(fname, last_name):
    return f"{fname} {last_name}"

# Store the return value in a variable
full_name = get_full_name("Zane", "Moon")
print(full_name)

def subtract(x, y):
    return x-y

res = subtract(1, 3)
print(res)

print("-----------------------")

# MC 3
print("MC 3")
def subtract(a, z):
    return a - z

res = subtract(100, 31)
print(res)

print("-----------------------")