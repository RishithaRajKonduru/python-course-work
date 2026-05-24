Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for var in seq:
    #stmts
    '''str,list,tuple,set,dict,range()'''

    
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    for var in seq:
NameError: name 'seq' is not defined. Did you mean: 'set'?
s='python programming'
for i in s:
    print(i)

    
p
y
t
h
o
n
 
p
r
o
g
r
a
m
m
i
n
g
l=[1,2,3,4,5,6]
for i in l:
    print(i)

    
1
2
3
4
5
6
t=(1,2,3,4,5,6)
for i in t:
    print(i)

    
1
2
3
4
5
6
s={1,2,3,4}
for j in s:
    print(j)

    
1
2
3
4
d={1:2,3:4,5:6}
for i in d:
    print(i)

    
1
3
5

for i in d:
    print(i,d[i])

    
1 2
3 4
5 6
s='python'
for i in enumerate(s):
    print(i)

    
(0, 'p')
(1, 'y')
(2, 't')
(3, 'h')
(4, 'o')
(5, 'n')
>>> for i in enumerate(s):
...     print(i[0],i[1])
... 
...     
0 p
1 y
2 t
3 h
4 o
5 n
>>> l=[12345,45678,56789,6578]
>>> for i in enumerate(l)"
SyntaxError: unterminated string literal (detected at line 1)
>>> for i in enumerate(l):
...     print(i[0],i[1],i)
... 
...     
0 12345 (0, 12345)
1 45678 (1, 45678)
2 56789 (2, 56789)
3 6578 (3, 6578)
>>> s={567,4567,34567,3456,3245,143}
>>> for i in enumerate(s):
...     print(s[i],i)
... 
...     
Traceback (most recent call last):
  File "<pyshell#60>", line 2, in <module>
    print(s[i],i)
TypeError: 'set' object is not subscriptable
>>> 
>>> 
>>> pin=1234
>>> for i in range(5):
...     entered_pin==int(input("enter the pin: "))
...     if entered_pin==pin:
...         print("unlock the phone")
...         break
...     else:
...         print("invalid pin")
... else:
