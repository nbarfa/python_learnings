import random
lst = ['s','w','g']

chance = 1
noc = 0
cp = 0
hp = 0

print("WELLCOME TO SNAKE,WATER,GUN GAME \n\n\n")
print("s for snake \n w for Water \n g for Gun \n\n")

while chance <= 10:
    chance = chance + 1
    a = input("Snake,Water,Gun : ")
    r = random.choice(lst)
    if a == r:
        print("Tie both 0 point \n")

    elif a =="s" and r =="g":
        cp = cp + 1
        print(f"your guess is {a} and computer guess is {r} \n")
        print("computer wins 1 point ")
        print(f"computer point is {cp} and your point is {hp} \n")
    elif a=="g" and r == "s":
        hp = hp+1
        print(f"your guess is {a} and computer guess is {r} \n")
        print("you wins 1 point ")
        print(f"computer point is {cp} and your point is {hp} \n")
    elif a=="w" and r =="s":
        cp = cp+1
        print(f"your guess is {a} and computer guess is {r} \n")
        print("computer wins 1 point \n ")
        print(f"computer point is {cp} and your point is {hp} \n")
    elif a=="s" and r=="w":
        hp = hp+1
        print(f"your guess is {a} and computer guess is {r} \n")
        print("you wins 1 point ")
        print(f"computer point is {cp} and your point is {hp} \n")
    elif a =="g" and r == "w":
        cp = cp+1
        print(f"your guess is {a} and computer guess is {r} \n")
        print("computer wins 1 point ")
        print(f"computer point is {cp} and your point is {hp} \n")
    elif a == "w" and r == "g":
        hp = hp+1
        print(f"your guess is {a} and computer guess is {r} \n")
        print("you wins 1 point ")
        print(f"computer point is {cp} and your point is {hp} \n")
    else:
        print("You entered wrong enter (s:-snake),(g:-gun),(w:-water)")

#noc = noc +1
#print(f"{chance - noc} is left out {chance} \n ")

print("Game Over")
if cp > hp:
    print("computer wins you loose ")
elif cp < hp:
    print("computer loose you wins ")
else:
    print("Both computer and your point is same ")
print(f"your point is {hp} and computer point is {cp} ")

