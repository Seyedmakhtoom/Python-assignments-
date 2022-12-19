import random
n=int(input("Please specify the length of the array"))
a = int(input("Please enter the range of numbers: "))
p = []

while True:
    b = random.sample(range(0,a),n)
    p.append(a)   
    
    print(b)
    break