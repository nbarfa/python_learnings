# Question 1

'''a = "Good Morning"
b = input("Entre Your Name : ")
print(a,b)'''

# Question 2

'''name = input("Entre your name : ")
date = input("Entre the date : ")
letter ='Dear <|Name|>,\nYou are selected,\nDate'
letter = letter.replace("<|Name|>",name)
letter = letter.replace("Date",date)

print("\nYour letter")
print(letter)'''

# Question 3,4

'''str = input("Entre a string : ")
#double_space_index = str.find("  ")
modified = str.replace("  "," ")
print(modified)'''

# Question 5

letter = "Dear Harry,This python course is nice, Thanks!"
formatted_letter = ("Dear Harry, \nThis python course is nice \nThanks!")
print("Before formating","\n",letter,"\n After Formating","\n",formatted_letter)