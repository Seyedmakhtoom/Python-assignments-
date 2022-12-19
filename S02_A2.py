import random

pc = random.randint(1,6)
prize = random.randint(1,6)


while True:
    if pc != 6:
        print("The dice number: ", pc)
        break
    else:
        print("The dice number is:", pc, "\nWell Done", "\nYour prize is: ", prize)
        break