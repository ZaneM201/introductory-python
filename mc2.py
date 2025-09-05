x = int(input("Enter the value for x:"))
y = int(input("Enter the value for y:"))

#Convensional If Else Statement
if x == y:
    print("They're the same!")
else:
    print("They're different!")

#Short hand if-else (Ternary Operators or Conditional Expressions)
print("They're the same!") if x == y else print("They're different!")