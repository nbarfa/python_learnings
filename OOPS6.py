'''class Dad():
    basketball = 3
class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes I can dance {self.dance} no. of dance steps."
class Grandson(Son):
    dance = 5
    #def isdance(self):
        #return f"Yes||Yes I can dance {self.dance} no. of dance steps. "
darry = Dad()
garry = Son()
larry = Grandson()

print(larry.isdance())'''


# Quiz
class electronic():
    device = 4
    def electro(self):
        return f"No. of electronic devices {self.device}"

class phone(electronic):
    phone = "Oppo A79"
    def pho(self):
        return f"The device name is {self.phone}"
class pocketdevice():
    poket = ["Charging cable ","Adopter","Headset","Phone Case"]
    def pokdev(self):
        return f"This device include {self.poket}."

device = electronic()
phone_name = phone()
with_phone = pocketdevice()

print(phone_name.pocketdevice())