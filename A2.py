class color:
    Yellow = '\33[033m' 


a = float(input("Please enter your first dimension: "))
b = float(input("Please enter your second dimension: "))
c = float(input("Please enter your third dimension: "))

if a <= b + c and b <= a + c and c <= a + b:
   print(color.Yellow + "Valid dimension ")
else:  
    print(color.Yellow + "Invalid dimension ")