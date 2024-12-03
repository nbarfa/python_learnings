class Employee:
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Employe name is {self.name}.His salary is {self.salary}.His role is {self.role}."

    def __repr__(self):
        return f"Employe('{self.name}',{self.salary},'{self.role}')"

    def __str__(self):
        return f"Employe name is {self.name}.His salary is {self.salary}.His role is {self.role}."



emp1 = Employee("Nitin",3000,"Instructor")
emp2 = Employee("Aman","40000","Programer")
print(emp1)

