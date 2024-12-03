def funargs(normal,*args,**kwargs):
    print(normal)

    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

nit = ["Yash","Aman","Nitin","Jay","Bhupendra"]
normal = "This is normal "
a = {"Yash":"cook","Jay":"coordinator","Aman":"Monitor"}
funargs(normal,*nit , **a)