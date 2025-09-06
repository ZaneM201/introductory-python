#if else statements
# Execute some logic or instructions if (and only IF) the condition is met
# We can catch with an else in case that the condition doesn't match
# Equals: a == b
# Not Equals: a != b
# Less Than: a < b
# Greater Than: a > b
# Less than or equal: a <= b
# Greater than or equal: a >= b
age = 24

if age < 100:
    if age < 21:
        print("You're a minor without access!")
    else:
        print("Your're young!")
elif age == 100:
    print("Congratulations, you got to live a century!")
else:
    print("Sorry, you're getting old!")

# Exercise
x = 8
y = 8
if x >= y:
    print("Hello")
else:
    print("Welcome")

x = "hello"
y = "hello"

if x == y:
    print("It's the same word")
else:
    print("They're different")