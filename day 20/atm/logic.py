
data={
    123456:{'pin':1234,'balance':5000,'name':'charan','history':[]},
    234561:{'pin':1234,'balance':8000,'name':'Pavithra','history':[]},
    345621:{'pin':1234,'balance':7000,'name':'Sreeja','history':[]},
    }


def login():
    acc_num=int(input("Enter the account number:"))
    pin=int(input("Enter the pin:"))
    if acc_num in data and data[acc_num]['pin']==pin:
        print("Login successful")
        return False
    else:
        print("Login Failed.
    
