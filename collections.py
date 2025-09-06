# Python Collections
# A group of data elements in python that allows us to store multiple data in a single variable
# lists, tuples, dictionaries, set

# 1. Lists -  They're used to store multiple items in a single variable
# and they are difined by square brackets []
# Properies: list are ordered, changeable (or mutable) and allow duplicates and they're index based
empty_list = []
print(f"Collection data type: {type(empty_list)}")

fruits_list = ["apple", "banana", "cherry", "orange", "banana"] #this is a list with default values
#                0         1          2         3         4
print(f"Empty List: {empty_list}")
print(f"List: {fruits_list}")
print(f"Retreiving a value: {fruits_list[3]}")
print(f"List length: {len(fruits_list)}")