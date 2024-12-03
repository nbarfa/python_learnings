import random

lst = ['s', 'w', 'g']

chance = 1
noc = 10        
cp = 0
hp = 0

print("WELCOME TO SNAKE, WATER, GUN GAME \n\n\n")
print("s for Snake \n w for Water \n g for Gun \n\n")

while chance <= noc:
    print(f"Chance {chance} of {noc}")
    a = input("Snake, Water, Gun: ")
    r = random.choice(lst)
    if a == r:
        print("Tie, both 0 point\n")
    elif a == "s" and r == "g":
        cp += 1
        print(f"Your guess is {a} and computer's guess is {r}\n")
        print("Computer wins 1 point")
    elif a == "g" and r == "s":
        hp += 1
        print(f"Your guess is {a} and computer's guess is {r}\n")
        print("You win 1 point")
    elif a == "w" and r == "s":
        cp += 1
        print(f"Your guess is {a} and computer's guess is {r}\n")
        print("Computer wins 1 point\n")
    elif a == "s" and r == "w":
        hp += 1
        print(f"Your guess is {a} and computer's guess is {r}\n")
        print("You win 1 point")
    elif a == "g" and r == "w":
        cp += 1
        print(f"Your guess is {a} and computer's guess is {r}\n")
        print("Computer wins 1 point")
    elif a == "w" and r == "g":
        hp += 1
        print(f"Your guess is {a} and computer's guess is {r}\n")
        print("You win 1 point")
    else:
        print("You entered the wrong input. Please enter (s: Snake), (g: Gun), (w: Water)")

    print(f"Computer's points: {cp} | Your points: {hp}\n")
    print(f"Chances left: {noc - chance}\n")
    chance += 1

print("Game Over")
if cp > hp:
    print("Computer wins, you lose!")
elif cp < hp:
    print("Computer loses, you win!")
else:
    print("It's a tie!")

print(f"Your points: {hp} | Computer's points: {cp}")
