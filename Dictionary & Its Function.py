#d1 = {"Nitin":"Roti","Yash":"Burger","Aman":"Maggie","Sachin":{"Bf":"Bread","Lunch":"roti","Din":"Chaval"}}
#print(d1)
#d1["Ankit"]="Junk Food"
#print(d1)
#del d1["Ankit"] #To delete anything in ditionary
#print(d1)

# Dictionary Functions

#d2 = d1.copy()  #Used to copy dictionary
#print(d2)
#print(d1.get("Nitin"))  # It will give the value of Niitn
#d1.update({"Arjun": "Milk"})
#print(d1)
#print(d1.keys()) #It will print the keys of dictionary

# Question 1
dic1 = {"sets":"Collection Of Data",
        "Mutable":"Can Change",
        "Immutable":"Cannot Change"}
nit = input("Entre A Word : ")
print(dic1[nit])