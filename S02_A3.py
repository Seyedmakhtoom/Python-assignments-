import random 


a = int(input("please enter the length of array:  "))
b = int(input("Please enter the range of random number: "))


lst = []

for i in range(a):
    Num = random.randint(0,b)
    lst.append(Num)

    
print(lst)












