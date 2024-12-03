'''list1 = [["Nitin",23],["Yash",34],["Aman",56],["Jay",87]]
dic1 = dict(list1)
print(dic1)
for item in dic1.items():
    print(item)
'''

# Quiz

items = [int,float,"Nitin",5,6,3,8,90,100,345,2345,678,9080]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)