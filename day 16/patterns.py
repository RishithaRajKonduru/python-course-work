'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=' ')
    print()'''


'''n=int(input("enter the number:"))
c=1
for i in range(n):
    for j in range(i+1):
        print(c,end=' ')
        c+=1
    print()'''


'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(i+1):
        print(i*j,end=' ')
    print()'''


'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print()'''

'''n=int(input("enter the size:"))
c=65
for i in range(n):
    for j in range(i+1):
        print(chr(c),end=' ')
        c+=1
    print()'''

'''#12 20 36 42 55 67 74 83 98 101
l=[12,20,36,42,55,67,74,83,98,101]
i=0
while i<len(l):
    if l[i]==74:
        print(l[i],'found at index:',i)
        break
    i+=1
else:
        print('74 is not found')'''


'''l=[120,220,36,42,545,67,724,83,98,101]
i=0
m=0
while i<len(l):
    if l[i]>m:
        m=l[i]
    i+=1
print(m)'''


'''l=[120,220,36,42,545,67,724,83,98,101]
i=0
j=len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1'''


#list comprehension
'''l=[1,2,3,4,5,56,6,7]
res=[i+10 for i in l]
print(res)'''

'''l=[1,2,3,4,5,56,6,7]
res=[i*l[i] for i in range(len(l))]
print(res)'''


'''l=[1,2,3,4,5,56,6,7]
res=[i**3 for i in l]
print(res'''


'''l=[1,2,3,4,5,56,6,7]
res=[i**3 for i in l if i%2==0]
print(res)'''


'''l=[1,2,3,4,5,56,6,7]
res=[i if i%2==0 else 0 for i in l]
print(res)'''




