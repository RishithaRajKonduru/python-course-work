'''i=1
while i<=10:
    print(i)
    i+=1
'''

'''l=[1,2,0,3,0,4,5,0,2,0,4,20,2,12,0,45,12]
while 0 in l:
    l.remove(0)
print(l)'''


'''i=100
while i>=2:
    print(i)
    i-=2'''

#table of a given number
'''n=int(input("enter the number: "))
i=1
while i<=10:
    print(f'{n}*{i}={n*i}')
    i+=1'''


'''i=1
while i<=10:
    i+=1
    if i==5:
        continue
    print(i)'''

#sum of numbers
'''n=int(input("enter the number :"))
sum=0
while n>0:
    sum+=n%10
    n//=10
print("sum of digits:",sum)'''
    
 #factorial
'''n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)'''

#factors of numbers
'''n=int(input("enter the number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')'''

#next letter
'''n=input("enter the string:")
res=''
for i in n:
    res+=(chr(ord(i)+1))
print(res)'''

#o/p:code e3 d2 o1 c0
'''n=input("enter the string:")
i=len(n)-1
while i>=0:
    print(n[i],i)
    i-=1'''


#first non-repiting character
'''n=input("enter the string:")
for i in n:
    if n.count(i)==1:
        print(i)
        break
else:
    print("all are re mul times")'''

#reverse the number using while loop
n=int(input("enter the number:"))
res=0
while n>0:
    rem=n%10
    res=res*10+rem
    n//=10
print(res)
    
