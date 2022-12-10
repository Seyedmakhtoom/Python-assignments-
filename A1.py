import math

t = input("Please choose which operation do you ccarry out: ") 
if t == "1":
    x = float(input("Please enter the number: "))
    op = input("Please choose operation: ")

    if op == "sine":
        result = math.sin(math.radians(x))
    if op == "cos":
        result = math.cos(math.radians(x))
    if op == "tan":
        result = math.tan(math.radians(x))
    if op == "cot":
        result = math.cot(math.radians(x))
    if op == "r" and x > 0:
        result = math.sqrt(x)
    else:
        print("Error")
    if op == "f":
        if x == 0 and x == 1:
            print("1")
        x = int(x);
        result = math.factorial(x)
    
    print(result)
 
if t == "2":
    a = float(input("Please enter the number: "))
    b = float(input("Please enter the number: "))
    op = input("Pleas enter operation: ")

if op == "+":
    result = a + b 
if op == "-":  
    if a >= b:
        result = a - b
    else:
        print("Error")
if op == "*":
    result = a * b 
if op == "/":
    if a >= b:
        result = a / b
    else:
        print("Error") 

print(result)
