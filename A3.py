class color:
    yellow = '\33[033m'

name = input("Please enter your name: ")
family = input("Please enter your family: ")

G1 = float(input("Please enter your grade 1: "))
G2 = float(input("Please enter your grade 2: "))               # G1, G2, G3 >>>> the grade of leason 1, 2, 3
G3 = float(input("please enter your grade 3: "))

GPA = (G1 + G2 + G3) / 3

print("your GPA is: ", GPA)

if GPA >= 17:
   print(color.yellow + "You have done great")
if GPA < 17 and GPA > 12:
    print(color.yellow + "You have done normall")
if GPA < 12:
    print(color.yellow + "You're fail")
    
