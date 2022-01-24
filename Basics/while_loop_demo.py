# Used to iterate block of code as long as test expression is true
# test expression is checked first, if expression is evaluated to true then body of loop
# Conditions are used to stop the loops
# Can iterate onlist , strings, tuples, dictionary
# While test_expression:
# body of while loop

# x=int(input("Enter the value:"))
# while x<=10:
#     print(x)
#     x=x+1
#     print("inside while")
# print("out of while loop")

city = "Melbourne"
x = 0
while x < len(city):
     print(city[x])
     x = x + 1

