'''n=int(input("enter the size:"))
for row in range(n):
    for col in range(n):
        print('*',end=' ')
    print()'''

'''n=int(input("enter the size:"))
for row in range(n):
    for col in range(row+1):
        print('*',end=' ')
    print()'''


'''n=int(input("enter the size:"))
for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()'''

'''n=int(input("enter the size:"))
for row in range(n):
    for s in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print('*',end=' ')
    print()'''

'''n=int(input("enter the size:"))
for row in range(n):
    for s in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*',end=' ')
    print()'''

'''n=int(input("enter the size:"))
for row in range(n):
    for col in range(n):
        print(int(col%2==0),end=' ')
    print()'''


'''n=int(input("enter the size:"))
for row in range(n):
    for col in range(n):
        print(int(col%2!=0),end=' ')
    print()'''

'''n=int(input("enter the size:"))
for row in range(n):
    for col in range(n):
        print(int((row+col)%2==0),end=' ')
    print()'''

'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==(n-1) or j==0 or j==(n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ' )
    print()'''

'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==(n-1) or j==0 or j==(n-1) or n//2==i or n//2==j:
            print('*',end=' ')
        else:
            print(' ',end=' ' )
    print()'''


'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''n=int(input("enetr the size:"))
for i in range(n):
    for j in range(n):
        if i+j==(n-1) or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or(i==(n-1) and j<=n//2) or (j==n//2 and i>=n//2) or (i==n//2 and j>=n//2) or j==n-1 or i>=n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()




