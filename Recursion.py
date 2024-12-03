# Recursion :- It is a techique where function call itself in order to solve problem
# Example 1
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Entre a number : "))
print(f"Factorial of this number is : {factorial(num)}")
