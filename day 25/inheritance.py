
#single inheritance
'''class A:
    def printa(self):
        print("Parent class-A")
class B(A):
    def printb(self):
        print("Child class-B")

b=B()
b.printb()
b.printa()'''

#hierarchial inheritance

'''class A:
    def printa(self):
        print("Parent class-A")
class B(A):
    def printb(self):
        print("Child class-B")
class C(A):
    def printc(self):
        print("Child class-C")
class D(A):
    def printd(self):
        print("Child class-D")

b=B()
b.printb()
b.printa()

b=C()
b.printc()
b.printa()

b=D()
b.printd()
b.printa()'''



#multiple inheritance
'''class A:
    def printa(self):
        print("Parent class-A")
class B:
    def printb(self):
        print("Child class-B")
class C:
    def printc(self):
        print("Child class-C")
class D(A,B,C):
    def printd(self):
        print("Child class-D")

d=D()
d.printd()
d.printa()
d.printb()
d.printc()'''


#multilevel inheritance

'''class A:
    def printa(self):
        print("Parent class-A")
class B(A):
    def printb(self):
        print("Child class-B")
class C(B):
    def printc(self):
        print("Child class-C")

c=C()
c.printa()
c.printb()
c.printc()'''



#hybrid inheritance
'''class A:
    def printa(self):
        print("Parent class-A")
class B:
    def printb(self):
        print("Child class-B")
class C(B,A):
    def printc(self):
        print("Child class-C")
class D(C):
    def printd(self):
        print("Child class-D")

d=D()
d.printa()
d.printb()
d.printc()
d.printd()'''


'''class InstagramV1:
    def post(self):
        print("you can uploaqd posts")
    def reel(self):
        print("you can upload reels")

class InstagramV2(InstagramV1):
    def story(self):
        print("you can upload stories")
    def live(self):
        print("you can go for live")


dhanu=InstagramV1()
print("dhanu-Instagram v1")
dhanu.post()
dhanu.reel()

charan=InstagramV2()
print("\ncharan-Instagram v2")
charan.post()
charan.reel()
charan.story()
charan.live()'''


'''class InstagramV1:
    def post(self):
        print('you can upload posts')
    def reel(self):
        print('you can upload the reels')
class InstagramV2(InstagramV1):
    def story(self):
        print('you can upload story')
    def live(self):
        print('you can go for the live')

class Whatsapp:
    def wtstatus(self):
        print('you can upload whatsapp status')
class facebook:
    def fbstory(self):
        print('you can upload facebook story')

class InstagramV3(InstagramV2,Whatsapp,facebook):
    def crossplatforms(self):
        print('you can upload same story on your whatsapp status ')
        print('you can upload same story on your facebook story ')    

sreeja=InstagramV1()
print('sreeja - InstagramV1')
sreeja.post()
sreeja.reel()

varun=InstagramV2()
print('\nvarun - InstagramV2')
varun.post()
varun.reel()
varun.story()
varun.live()

charan=InstagramV3()
print('\ncharan - InstagramV3')
charan.post()
charan.reel()
charan.story()
charan.live()
charan.wtstatus()
charan.fbstory()
charan.crossplatforms()'''



'''class A:
    def print(self):
        print("class-A")
class B(A):
    def print(self):
        super().print()
        print("class-B")
b=B()
b.print()'''



'''class A:
    def print(self):
        print("class-A")
class B:
    def print(self):
        print("class-B")
class C(A,B):
    def print(self):
        A.print(self)
        B.print(self)
        print("class-C")
c=C()
c.print()'''


'''class InstagramV1:
    def post(self):
        print('you can upload posts')
    def reel(self):
        print('you can upload the reels')
class InstagramV2(InstagramV1):
    def story(self):
        print('you can upload story')
    def live(self):
        print('you can go for the live')

class Whatsapp:
    def wtstatus(self):
        print('you can upload whatsapp status')
class facebook:
    def fbstory(self):
        print('you can upload facebook story')

class InstagramV3(InstagramV2):
    def note(self):
        print('you can update the note')
        
class InstagramV4(InstagramV2):
    def instants(self):
        print('you can update the snap')
        
class InstagramV5(InstagramV3,InstagramV4,Whatsapp,facebook):
    def crossplatforms(self):
        print('you can upload same story on your whatsapp status ')
        print('you can upload same story on your facebook story ')    

sreeja=InstagramV1()
print('sreeja - InstagramV1')
sreeja.post()
sreeja.reel()

varun=InstagramV2()
print('\nvarun - InstagramV2')
varun.post()
varun.reel()
varun.story()
varun.live()

charan=InstagramV5()
print('\ncharan - InstagramV3')
charan.post()
charan.reel()
charan.story()
charan.live()
charan.wtstatus()
charan.fbstory()
charan.crossplatforms()


pranu=InstagramV5()
print('\npranu - InstagramV4')
pranu.post()
pranu.reel()
pranu.story()
pranu.live()
pranu.wtstatus()
pranu.fbstory()
pranu.note()
pranu.instants()
pranu.crossplatforms()'''
