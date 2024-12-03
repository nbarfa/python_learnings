#a = 9
#b = 1
#c = sum((a,b))

def function1(a,b):
    print("Hello you are in function1")

def function2(a,b):
    """ This is the function which will calculate average of two number """
    average = (a+b)/2
    # print(average)
    return average
function2(5,5)
#print(v)
print(function2.__doc__)