'''class stud:
    pass
nitin = stud()
aman = stud()
nitin.name = "Nitin"
nitin.std = 12
nitin.section = "C"
aman.name = "Aman"
aman.std = 11
print(nitin.std,aman.std)'''

class Employee:
    no_of_leaves = 8
    pass

nitin = Employee()
aman = Employee()

nitin.name = "Nitin"
nitin.sallary = 25000
nitin.role =  "Instructor"

aman.name = "Aman Barfa"
aman.sallary = 30000
aman.role = "Accountent"

print(aman.no_of_leaves )
print(nitin.no_of_leaves )
print(Employee.no_of_leaves )
print(aman.__dict__ )