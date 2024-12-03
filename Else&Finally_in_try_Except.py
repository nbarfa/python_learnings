f1 = open("Nitin.txt")

try:
    f = open("does.txt")

except Exception as e:
    print(e)
else:
    print("This will run only when exception is not running ")


finally:
    print("Run this anyway.....")
    f1.close()


print("Runned Succesfully")