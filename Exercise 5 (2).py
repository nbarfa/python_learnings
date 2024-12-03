import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c == 1:
            value = input("Type here\n")
            with open("yash-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif c == 2:
            value = input("Type here\n")
            with open("yash_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c == 1:
            value = input("Type here\n")
            with open("aman-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif c == 2:
            value = input("Type here\n")
            with open("aman_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif k == 3:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c == 1:
            value = input("Type here\n")
            with open("nitin-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
        elif c == 2:
            value = input("Type here\n")
            with open("nitin_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    else:
        print("Please enter valid input (1 for Yash, 2 for Aman, 3 for Nitin)")


def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c == 1:
            with open("yash-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("yash_food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c == 1:
            with open("aman-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("aman_food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("Enter 1 for exercise and 2 for food: "))
        if c == 1:
            with open("nitin-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("nitin_food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("Please enter valid input (1 for Yash, 2 for Aman, 3 for Nitin)")


while True:
    print("Health Management System:")
    a = int(input("Enter 1 to log value and 2 to retrieve: "))
    if a == 1:
        b = int(input("Enter 1 for Yash, 2 for Aman, 3 for Nitin: "))
        take(b)
    elif a == 2:
        b = int(input("Enter 1 for Yash, 2 for Aman, 3 for Nitin: "))
        retrieve(b)
    else:
        print("Invalid choice. Please enter 1 or 2.")

    con = input("Do you want to continue (yes/no): ").strip().lower()
    if con != 'yes':
        print("Exiting Health Management System. Goodbye!")
        break
