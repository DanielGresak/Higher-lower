import random

cmpnum = random.randint(1,100)
print(cmpnum)

usernumber = "x"

while usernumber is not cmpnum:
    usernumber = int(input("enter a number: "))
    if usernumber == cmpnum:
        print("you win")
    elif usernumber < cmpnum:
        print("Higher")
    elif usernumber > cmpnum:
        print("lower")

print("you are the best... around")