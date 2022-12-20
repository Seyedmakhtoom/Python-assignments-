import random
 
print("Take turns throwing the dice, everyone has only one chance to roll the dice ")

while True:
    a = input("if you wanna roll it type the word yes: ")
    if a == "yes":
        dice = random.randint(1,6)
        print(dice)
        if dice == 6:
            print("You Win, you are able to roll the dice two more times")
            a = input("if you wanna take your chances press y on your keyboard: ")
            if a == "y":
                for i in range(2):
                    dice = random.randint(1,6)
                    print(dice)
            if dice != 6:
                print("Your chance to roll the dice is over")
                break    
    else:
        print("You left the program")
        break      


