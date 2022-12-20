import random

pc = random.randint(0, 20)
count = 1

while True:
    user = int(input("Please enter the number: "))
    if user == pc:
        print("Wiiinnnnnnn", "\nYour efforts are", count, "times")
        count = count + 1
        break
    elif user > pc:
        print("Get back")
        print("Your efforts are", count, "times")
        count = count + 1
    elif user < pc:
        print("Go ahead")
        print("Your efforts are", count, "times")
        count = count + 1
for i in range(5):
    print("I", " \n\tHope", "\n\t\tYou", "\n\t\t\tenjoyed", "\n\t\t\t\tthe game")
