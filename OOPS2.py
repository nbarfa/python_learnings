class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetail(self):
        return f"Employe name is {self.name}.\nHis salary is {self.salary}.\nHis role is {self.role}."

nitin = Employee("Nitin Barfa", 25000, "Instructor")
aman = Employee("Aman Barfa", 35000, "Accountent")

'''nitin.name = "Nitin"
nitin.salary = 25000
nitin.role =  "Instructor"

aman.name = "Aman Barfa"
aman.salary = 30000
aman.role = "Accountent" '''

print(nitin.salary)