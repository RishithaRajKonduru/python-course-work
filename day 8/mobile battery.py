#mobile battery
'''ch=int(input("enter the battery per:"))
if ch<=20:
       print("Alert:Battery is low")
'''

#discount
'''discount=int(input("enter the discount:"))
price=int(input("enter the price:"))
if discount:
    price-=price*(discount/100)
    print("discount applied")
print(price)
'''
#login
'''data={

    'niharika@gmail.com':'ni@123',
    'charan@gmail.com':'ch@123',
    'pavitra@gmail.com':'pa@123',
    }
email=input("Enter the email:")
password=input("Enter the password:")
if data.get(email)==password:
    print("Login successful")
else:
    print("Login Invalid")
'''
#otp
'''import random
otp=random.randint(1111,9999)
print("your otp:",otp)
entered_otp=int(input("enter the otp:"))
if otp==entered_otp:
    print("verified succesfully")
else:
    print("Invalid OTP")'''

#order fare
'''hr,min=list(map(int,input("Enter the time(HH:MM:").split(':')))
fare=0
price=450
if 0<=hr<=23 and 0<=min<=59:
            if 8<=hr<=16:
                 fare=40
            elif 17<=hr<=23:
                 fare=100
            elif 0<=hr<=7:
                 fare=150
            print("total fare:",fare+price)
else:
            print("invalid time:")'''

#student exm
'''data={
    'saniya':{'status':True,'python':50,'mysql':80,'flask':89},
    'niharika':{'status':True,'python':90,'mysql':98,'flask':85},
    'charan':{'status':False,'python':None,'mysql':None,'flask':None},
    'surya':{'status':True,'python':40,'mysql':39,'flask':20},
    'pavithra':{'status':True,'python':55,'mysql':48,'flask':62},
    'sreeja':{'status':True,'python':68,'mysql':73,'flask':76},
    }
name=input("enter the student name:")
if name in data:
    print(name,'s report:')
    if data[name]['status']:
        avg=(data[name]['python']+data[name]['mysql']+data[name]['flask'])/3
        if avg>80:
            print('congratulations,well done')
        elif avg>60:
            print('good improvement needed')'''

'''sum=0
for i in range(1,11):
    value=2*i
    sum=sum+value
print("sum is ",sum)'''


'''print(int(input())*55)'''




       
