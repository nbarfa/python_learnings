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


class program(Employee):
    def __init__(self,aname,asalary,arole,alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguages
    def prog(self):
        return f"The Programmer name is {self.name}.His salary is {self.salary}.His role is {self.role}.Languages known {self.language}."


nitin = Employee("Nitin Barfa", 25000, "Instructor")
aman = Employee("Aman Barfa", 35000, "Accountent")
karan = program("Karan",40000,"Programmer",["Python","Java"])
piyush = program("Piyush",34000,"Programmer",["Python"])
print(karan.prog())