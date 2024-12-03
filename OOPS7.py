class A:
    classvar1 = "I am in class variable of class A"
    def __init__(self):
        self.var1 = "I am varible of class A"
        self.classvar1 = "instance var of class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am class variable of class B"
    def __init__(self):
        super:__init__()
        self.var1 = "I am variable of class B"
        self.classvar1 = "instance var of class B"


a = A()
b = B()
print(a.special,b.var1,b.classvar1)
