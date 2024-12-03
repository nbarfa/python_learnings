# Question 1

'''dic1 = {"Panni":"Water",
        "Diwar":"Wall",
        "Chabi":"Key",
        "Kursi":"Chair"
        }
hindi_word = input("Entre a Hindi word to look up its English translation : ")
translate = dic1.get(hindi_word,"Word not found in the dictonary....")
print(translate)'''

# Question 2

num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
num3 = int(input("Enter a number : "))
num4 = int(input("Enter a number : "))
num5 = int(input("Enter a number : "))
num6 = int(input("Enter a number : "))
num7 = int(input("Enter a number : "))
num8 = int(input("Enter a number : "))

number = [num1,num2,num3,num4,num5,num6,num7,num8]

unique = set(number)

print("\nThe unique numbers are : ",unique)