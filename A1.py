import math


a = float(input("Please enter a number: "))

op = input("Please enter operation: ")

if op == "radical":
    result = math.sqrt(a)
if op == "sine":
    result = math.sin(math.radians(a))
if op == "cos":
    result = math.cos(math.radians(a))
if op == "cot":
    result = math.cot(math.radians(a))
if op == "tan":
    result = math.tan(math.radians(a)) 
if op == "factorial":
    a= int(a);
    result = math.factorial(a)



print(result)


