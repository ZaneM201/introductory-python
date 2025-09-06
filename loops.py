# Loops: for and while
# Is used for iterating over a sequence (or collections like list, tuples, dictionaries, set, strings)
# Keywords -> continue - jumps to the next iteration, and break - finish the loop
# For: For iterating through collections, or iterate in order
# While: iterating untiol a condition is met

students = ["Reggie", "Zane", "Luis", "Giancarlo", "Kevin"]
found = False
iteration = 0
while not found: # False -> True
    #print(iteration)
    if students[iteration] == "Kevin": # students[0] == "Reggie" -> True
        found = True
        #print(f"Hey {students[iteration]} is here!")
    else:
        iteration+=1

fruits_list = ["apple", "banana", "cherry", "orange", "banana"]

#for fruit in fruits_list:
   # if fruit == "banana":
       # continue
    #else:
        #print(fruit)

#Range function - Allow us to iterate through a start, stop and step values
# start it's INCLUSIVE
# stop it's EXCLUSIVE
# step are the increments (e.g. 1, 2, 3, 4, 5... ect)

for x in range(10): #using range with the stop parameter only
    print(x)

for x in range(0,10,2):
    print(x)

for x in range(0,len(fruits_list),1):
    print(fruits_list[x])

name = "Zane"

for x in name:
    print(x)