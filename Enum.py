'''l1 = ["Yash","Aman","Nitin","Jay"]
for index,item in enumerate(l1):
    if (index%1==0):
        print(index,item)'''

'''list1 = ["Nitn","yash","Aman"]
for index,value in enumerate(list1):
    print(index,value)'''

list2 = ["Yash","Aman","Nitin","Jay"]
result = enumerate(list2,10)
print(list(result))