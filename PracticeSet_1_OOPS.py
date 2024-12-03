# Question 1

'''class Microsoft_employee:
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Empolyee name is {self.name}.His salary is {self.salary}.His role is {self.role}."

emp1 = Microsoft_employee("Ramesh Jain",24000,"Programmer")
emp2 = Microsoft_employee("Suresh Agrawal",45000,"Programmer")
emp2 = Microsoft_employee("Rajesh Dua",50000,"Programmer")

print(emp1.printdetails()) '''

# Question 2
import math
class Calculator:
    def __init__(self,number):
        self.number = number

    def find_squr(self):
        return self.number ** 2

    def find_cube(self):
        return self.number ** 3

    def find_root(self):
        return math.sqrt(self.number)


number = float(input("Entre a number : "))
cal = Calculator(number)

print(f"Square of {number} : {cal.find_squr()}")
print(f"Cube of {number} : {cal.find_cube()}")
print(f"Square Root of {number} : {cal.find_root()}")