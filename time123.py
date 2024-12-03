import time
initial = time.time()
k = 0
while(k<45):
    k+=1
    print("this is nitin")
print(f"while loop run in {time.time()-initial} ")
initial2 = time.time()
for i in range(45):
    print("this is nitin ")
print(f"foe loop run in {time.time()-initial2}")

