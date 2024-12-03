def dec(func1):
    def exe():
        print("Executing now")
        func1()
        print("Executed")
    return exe
@dec
def nit():
    print("Nitin")
nit()
