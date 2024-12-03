# File IO Basics
'''
"r" - open file for reading (r - read mode)
"w" - open file for weiting  (w - write mode)
"+" - open file for update (read and write both)
"x" - creates file if not exists if already exist operation fails (x - exclusive creation mode )
"a" - add more content to a file (a - append )
"t" - open file in text mode  (t - text mode )
"b" - open binary files (binary file - it contain data encoded in binary form it represent images,audio, video & other type of data)
'''

# File IO open(),read() & readline() for reading file
'''f = open("Nitin.txt","r")
content = f.read(437)
print("1",content)

content = f.read(437)
print("2",content)
f.close()'''

# readline()
'''f = open("Nitin.txt")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())'''

# File Writing And Appending
'''f = open("nitin2.txt","a")
a = f.write("My name is Nitin Barfa\n")
print(a)
f.close()'''

# Handle Read And Write Both
f = open("nitin2.txt","r+")
print(f.read())
f.write("Thank You")
