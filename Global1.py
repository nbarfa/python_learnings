'''a = 10 #Global
def function1(n):
    l = 5 #Local
    m = 2 #Local
    print(l,m)
    print(f"I have printed {n}")
function1("This is me ")
print(a)'''
x = 5
def yash():
    x = 10
    def aman():
        global x
        x = x + 30
    #print(f"Before calling aman {x}")
    aman()
    print(f"After calling aman {x}")
yash()
print(x)