'''i = 0

while (True):
    if i+1>5:
        i = i +1
        continue
    print(i+1, end=" ")
    if(i==50):
        break
    i = i + 1
'''

# Quiz

while(True):
    inp = int(input("Entre A Number : "))
    if inp>100:
        print("Congrates you have entred a number greater than 100")
        break
    else:
        continue

