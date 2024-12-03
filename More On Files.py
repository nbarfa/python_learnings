'''f = open("nitin2.txt","rb")
#print(f.tell())
print(f.readline())
#print(f.tell())
f.seek(11,1)
print(f.readline())
#print(f.tell())
f.close()'''

# Using With Block To Open Python Files

with open("nitin2.txt") as f, open("Nitin.txt ") as g:
    b = g.read()
    a = f.read()
    print(a,b)

f = open("nitin2.txt","rt")
print(f.readline())
f.close()
