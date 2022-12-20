sum = 0

while True:
    a = (input("Please enter the numbers: "))

    if a == "exit":
        print(sum)
        break
    p = float(a)
    
    sum = sum + p
