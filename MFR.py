# Map Function
'''num = ["3","90","23"]
num = list(map(int,num))
num[2] = num[2]+1
print(num[2])'''

'''num1 = [1,6,4,8,9,3,5]
num1 = list(map(lambda x:x*x,num1))
print(num1)'''

'''def square(a):
    return a*a
def cube(a):
    return a*a*a
func = [square,cube]
for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)'''

# Filter Function
'''list1 = [1,2,3,4,5,6,7,8,9,10]
def great(num):
    return num>5
greater = list(filter(great,list1))
print(greater)'''

# Reduce Function
from functools import reduce
list1 = [1,2,3,4]
num = reduce(lambda x,y:x+y, list1)
print(num)