'''def greet(name):
    print(f"Hello {name},Welcome to the python")
greet("Mounika")
greet("Charan")
greet("Sreeja")'''


'''def display(name,email,phonenumber):
    print(f'Name:{name}')
    print(f'Email:{email}')
    print(f'Phone Number:{phonenumber}')
display('charan','charan@gmail.com','9876543210')
display('charan@gmail.com','charan','9876543210')
display('9876543210','charan','charan@gmail.com')'''


'''def display(name,email,phonenumber):
    print(f'Name:{name}')
    print(f'Email:{email}')
    print(f'Phone Number:{phonenumber}')
    print()
display(name='charan',email='charan@gmail.com',phonenumber='9876543210')
display(email= 'charan@gmail.com',name='charan',phonenumber='9876543210')
display(phonenumber='9876543210',name='charan',email='charan@gmail.com')'''


'''def display(name,email,phonenumber=None,cgpa=None):
    print(f'Name:{name}')
    print(f'Email:{email}')
    print(f'Phone Number:{phonenumber}')
    print(f'CGPA:{cgpa}')
display('charan','charan@gmail.com','9876543210',8.8)
display('charan','charan@gmail.com','9876543210')
display('charan','charan@gmail.com')'''


'''def display(*names):
    print(names)
display('charan')
display('varun','dhanush')
display('sahil','niharika','pavithra','srishanth')
display('sreeja','anjali','priyanka')'''


'''def display(**names):
    print(names)
display(n1='charan')
display(n2='varun',n3='dhanush')
display(n4='sahil',n5='niharika',n6='pavithra',n7='srishanth')
display(n8='sreeja',n9='anjali',n10='priyanka')'''


'''n=int(input("enter the number:"))
c=0
for i in range(2,n//2+1):
    if n%i==0:
        c+=1
print("prime number" if c==0 else "not prime number")'''


'''def isPrime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input("enter the number:"))
print("Prime number" if isPrime(n) else "Not Prime number")'''


'''def check(s):
    vc=cc=dc=sc=0
    wc=1
    vol='aeiouAEIOU'
    for i in s:
        if i.isalpha():
            if i in vol:
                vc+=1
            else:
                cc+=1
        elif i.isdigit():
            dc+=1
        elif i.isspace():
            wc+=1
        else:
            sc+=1
    print(f"vol count: {vc}")
    print(f"con count: {cc}")
    print(f"dig count: {dc}")
    print(f"word count: {wc}")
    print(f"spc count: {sc}")
check("python programming language:version 3.14")'''
