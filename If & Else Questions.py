# Question 1 Write a Python if-else statement that prints "Even" if a number is even and "Odd" if a number is odd.
'''num =  int(input("Entre a number : "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
'''

# Question 2 Write a Python if-elif-else statement to check if a number is positive, negative, or zero.
'''num = int(input("entre a number : "))
if num > 0:
    print("Number is positive.")
elif num < 0:
    print("Number is negative.")
else:
    print("Number is Zero.")
'''

# Question 3  Write an if-else statement that checks if a given string is "hello" and prints "Greeting!" if it is, and "Not a greeting" if it isn't.
'''a = input("Entre A Word : ")
if a=="hello":
    print("Greeting")
else:
    print("Not a Greeting")
'''

# Question 4 Write an if-else statement that checks a boolean variable is_student and prints "Discount applied" if it is True and "No discount" if it is False.
'''stu = input("Are you a student yes/no : ")
is_student = stu == 'yes'
if is_student:
    print("Discount Applied")
else:
    print("Discount Not Applied ")
'''

# Question 5 Write a nested if-else statement to check if a number is within the range 1 to 100, and then whether it is an even or odd number.
'''num = int(input("Entre A Number : "))
if 1<= num <= 100:
    if num % 2 ==0:
        print("Number is within a range 1 to 100 and it is a even number")
    else:
        print("Number is within a range 1 to 100 and it is a odd number.")
else:
    print("Number is out of range 1 to 100.")
'''

# Question 6  Write an if-else statement using logical operators to check if a number is between 10 and 20 (inclusive) and print "In range" or "Out of range".
'''
num = int(input("Entre a Number : "))
if 10 <= num <= 20:
    print("In Range. ")
else:
    print("Out of the Range.")
'''

# Question 7 : Write an if-else statement to check if a character is a vowel ('a', 'e', 'i', 'o', 'u') and print "Vowel" or "Consonant".
'''
char = input("Entre a Character : ")
if char in ('a','i','o','u'):
    print("It is a vowel")
else:
    print("it is a consonant")
'''

# Question 8
'''num = int(input("Entre Your Age : "))
if num >= 18:
    print("You Are Elegible For Vote.")

else:
    print("You Are Not Elegible For Vote.")'''




