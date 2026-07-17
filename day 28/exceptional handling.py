#exceptional handling
#whenvever we think that error might occur we use "try block"
#to handle that error"except block"
#if thee are no errors else block will execute
#if there is an error or no error finally will execute
#------------single exception handling-----------------
'''try:
    if n>0:
        print("+ve number")
    else:
        print("-ve number")
except NameError:
    print("Define n")
else:
    print("No errors occured")
finally:
    print("End of the program")'''



'''try:
    n=10
    if n>0:
        print("+ve number")
    else:
        print("-ve number")
except NameError:
    print("Define n")
else:
    print("No errors occured")
finally:
    print("End of the program")'''


#--------multiple exception handling---------
'''try:
    n=10
    print(n)
    print(13+12)
    print(int(input("Enter the int:")))
    d={1:1,2:3,4:7}
    print(d[2])
    l=[34,456,134,3456]
    print(l[0])
    print(1/9)
except NameError:
    print("Define n")
except TypeError:
    print("give same datatype")
except ValueError:
    print("give proper datatype")
except KeyError:
    print("key is not present")
except IndexError:
    print("index is not there")
except ZeroDivisionError:
    print("you can't divide with zero")
else:
    print("No errors occured")
finally:
    print("End of the program")'''


'''try:
    n=10
    print(n)
    print(13+12)
    print(int(input("Enter the int:")))
    d={1:1,2:3,4:7}
    print(d[2])
    l=[34,456,134,3456]
    print(l[0])
    print(1/9)
except (NameError,TypeError, ValueError,KeyError,IndexError,ZeroDivisionError)as e:
    print("Error occured",e)
else:
    print("No errors occured")
finally:
    print("End of the program")'''

#instead of (NameError,TypeError, ValueError,KeyError,IndexError,ZeroDivisionError) we can use "Exception".

'''try:
    n=-10
    if n<0:
        raise Exception("Amount needs to be >0")
except Exception as e:
    print("Error occured:",e)
else:
    print("No errors occured")
finally:
    print("End of program")'''


