'''var1 = 50
var2 = 100
var3 = int(input())
if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")
'''

# Quiz
'''print("what is your  Age : ")
age = int(input())
if age<18<=100:
    print("you cannot  drive ")
elif age==18:
    print("We are not sure come and give the test")
elif age>100:
    print("you cannot drive")
else:
    print("you can drive ")
'''

# Question 2  FAULTY CALCULATOR
print("Entre 1st Number : ")
n1 = int(input())
print("Entre 2nd Number : ")
n2 = int(input())
print("So What You Want To Do +,-, /, %,*")
n3 = input()

if n1==45 and n2==3 and n3=="*" :
    print("555")
elif n1==56 and n2==9 and n3=="+":
    print("77")
elif n1==56 and n2==6 and n3=="/":
    print("4")
elif n3=="*":
    n4=n1*n2
    print(n4)
elif n3=="+":
    pl=n1+n2
    print(pl)
elif n3=="-":
    sub=n1-n2
    print(sub)
elif n3=="/":
    div=n2/n1
    print(div)
elif n3=="%":
    per=n2%n1
    print(per)
else:
    print("Out Of Range")
