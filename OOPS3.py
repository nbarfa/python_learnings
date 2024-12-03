class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole,anol):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.no_of_leaves = anol
    def printdetail(self):
        return f"Employe name is {self.name}.\nHis salary is {self.salary}.\nHis role is {self.role}.\nHis leaves is{self.no_of_leaves }"


    @classmethod
    def change(cls,new):
        cls.no_of_leaves = new



nitin = Employee("Nitin Barfa", 25000, "Instructor",1)
aman = Employee("Aman Barfa", 35000, "Accountent",3)

Employee.change(35)

print(aman.no_of_leaves)


