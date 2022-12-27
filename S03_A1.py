import random

num = int(input("Enter the lenght of array: "))
p = []
while len(p) < num:
    n = random.randint(0,20)
    p.append(n)

print(p)
 
delete = [set(p)]
print("This is the final result without duplicate numbers", delete)
