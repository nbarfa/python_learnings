num1 = input("Entre num1 ")
num2 = input("Entre num2 ")
try:
    print("the sum of this two number is ",
          int(num1) + int(num2))
except Exception as e:
    print(f"An Error Occoured: {e}")
print("this line is very important ")

# Question 1
# num1 = input("Entre a number 1 : ")
# num2 = input("Entre a number 2 : ")
# try:
#     result = int(num1) / int(num2)
#     print("Your Answer is : ",result)
# except Exception as ZeroDivisonError:
#     print("Soory ! YOu are dividing by zero. ")