
#method overriding
'''class Hotstar:
    def __init__(self,name):
        self.name=name
        print(f'Hello {self.name},Welcome to the hotstar----------')
    def login(self):
        print("you can login")
    def search(self):
        print("you can search")
    def categories(self):
        print("you can see the divisions")
    def playcontrollers(self):
        print("you can pause,resume and play")
    def livesports(self):
        print("you can watch the sports on live")
    def ads(Self):
        print("ads will run")
    def movies(self):
        print("limited movies")
    def downloads(self):
        print("can't download")
    def quality(Self):
        print("clrty will be limited")
class PremiumUser(Hotstar):
    def __init__(self,name):
        self.name=name
        print(f'Hello {self.name},Welcome to the hotstar premium-----------')
    def ads(self):
        print("ads will not run")
    def movies(self):
        print("unlimited movies")
    def downloads(self):
        print("can download and watch offline")
    def quality(self):
        print("clrty will be high")
charan=Hotstar('charan')
charan.login()
charan.search()
charan.categories()
charan.playcontrollers()
charan.livesports()
charan.ads()
charan.movies()
charan.downloads()
charan.quality()
surya=PremiumUser('surya')
surya.login()
surya.search()
surya.categories()
surya.playcontrollers()
surya.livesports()
surya.ads()
surya.movies()
surya.downloads()
surya.quality()'''


#method overloading

'''class Number:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __eq__(self, other):
        return self.num == other.num

    def __lt__(self, other):
        return self.num < other.num

    def __gt__(self, other):
        return self.num > other.num


a = Number(10)
b = Number(20)

print(a + b)
print(a - b)
print(a * b)
print(a == b)
print(a > b)
print(a < b)'''


#abstraction

'''from abc import ABC, abstractmethod

class Phonepay(ABC):

    def input(self):
        print("You can scan or enter the number")

    def amount(self):
        print("Enter the amount to pay")

    def pin(self):
        print("Enter the pin")

    @abstractmethod
    def verification(self):
        pass

    def paymentstatus(self):
        print("Amount transferred successfully / failed")


class HDFC(Phonepay):

    def verification(self):
        print("Verification completed through HDFC")


class SBI(Phonepay):

    def verification(self):
        print("Verification completed through SBI")


class UNION(Phonepay):

    def verification(self):
        print("Verification completed through UNION")


saniya = HDFC()
saniya.input()
saniya.amount()
saniya.pin()
saniya.verification()
saniya.paymentstatus()


tina = SBI()
tina.input()
tina.amount()
tina.pin()
tina.verification()
tina.paymentstatus()

rina = UNION()
rina.input()
rina.amount()
rina.pin()
rina.verification()
rina.paymentstatus()'''

















































































































































