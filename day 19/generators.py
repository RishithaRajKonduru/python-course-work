#12-1 2 3 4 6 12
'''def factors(n):
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res
def generators(res):
    for i in res:
        yield i
r=factors(38)
g=generators(r)
for i in range(len(r)):
    print(next(g))'''

#reverse list
'''def generators(res):
    for i in range(len(res)-1,-1,-1):
        yield res[i]
l=eval(input("enter the list:"))
g=generators(l)
for i in range(len(l)):
               print(next(g),end=' ')'''


'''def even(l):
    return list(filter(lambda i:i%2==0,l))
def gen(l):
    for i in l:
        yield i
l=[1,2,3,4,5,6,7,8,9,10,23,34,56,13,17,23,12,4,78,90,12,545,56]
e=even(l)
g=gen(e)
for i in range(len(e)):
    print(next(g))'''


'''def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))'''


'''def count(n):
    if n==0:
        return 0
    return 1+count(n//10)
print(count(567892345))'''


'''def power(n,base):
    if base==0:
        return 1
    return n*power(n,base-1)

print(power(8,4))'''






