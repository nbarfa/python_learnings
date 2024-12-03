class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"The employee is {self.fname} {self.lname}"


    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set..."
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("Setting Now.....")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

emp1 = Employee("Nitin","Barfa")
print(emp1.email)
emp1.fname = "Aman"
print(emp1.email)
emp1.email = "Yash.Barfa@gmail.com"

print(emp1.email)

del emp1.email
print(emp1.email)