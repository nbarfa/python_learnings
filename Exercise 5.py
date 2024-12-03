# Health Mangement System
import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c = int(input("enter 1 for exercise and 2 for food : "))
        if (c==1):
            value = input("type here\n")
            with open("yash-ex.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("yash_food.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("successfully written")
    elif k==2:
            c = int(input("entre 1 for exercise and 2 for food : "))
            if(c==1):
                value = input("type here\n")
                with open("aman-ex.txt","a") as op :
                    op.write(op.write(str([str(gettime())])+":"+value+"\n"))
                print("succesfully written")
            elif(c==2):
                value = input("type here\n")
                with open("aman_food.txt","a") as op:
                    op.write(str([str(gettime())]) + ":" + value + "\n")
                print("successfully entered ")
    elif k==3:
            c = int(input("entre1 for exercise and 2 for food : "))
            if(c==1):
                value = input("type here\n")
                with open("nitin-ex.txt","a") as op:
                    op.write(str([str(gettime())]) + ":" + value + "\n")
                print("successfully entred ")
            elif(c==2):
                value = input("type here\n")
                with open("nitin_food.txt","a"):
                    op.write(str([str(gettime())]) + ":" + value + "\n")
                print("successfully entred ")
    else:
        print("plz entre valid input ( 1(yash),2(aman),3(aman) ) ")
def retrieve(k):
    if k==1:
        c = int(input("entre 1 for exercise and 2 for food "))
        if(c==1):
            with open("yash-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("yash_food.txt") as op:
                for i in op:
                    print(i,end="")
    elif k==2:
        c = int(input("entre 1 for exercise and 2 for food "))
        if(c==1):
            with open("aman-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("aman_food.txt") as op:
                for i in op:
                    print(i,end="")
    elif k==3:
        c = int(input("entre 1 for exercise and 2 for food "))
        if(c==1):
            with open("nitin-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("nitin_food.txt") as op:
                for i in op:
                    print(i,end="")
    else:
        print("plz entre valid input (yash,aman,nitin)")
print("Health Management System : ")
a = int(input("enter 1 for log value and 2 for reteieve : "))
if(a==1):
    b = int(input("entre 1 for yash 2 for aman 3 for nitin : "))
    take(b)
else:
    b  = int(input("entre 1 for yash 2 for aman 3 for nitin : "))
    retrieve(b)




