class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetail(self):
        return (f"Employe name is {self.name}.\nHis salary is {self.salary}.\nHis role is {self.role}.")

    @classmethod
    def change(cls,new):
        cls.no_of_leaves = new

    @classmethod
    def from_str(cls,string):
        #params = string.split("-")
        #return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
    @staticmethod
    def sm(string):
        print("This is good ")


nitin = Employee("Nitin Barfa", 25000, "Instructor")
aman = Employee("Aman Barfa", 35000, "Accountent")
karan = Employee.from_str("Karam-40000-Instructur")
Employee.change(35)
print(karan.name)
print(aman.no_of_leaves)