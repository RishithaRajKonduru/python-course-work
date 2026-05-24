Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
names='sravani niharika pavithra'
names
'sravani niharika pavithra'
names.spltt()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    names.spltt()
AttributeError: 'str' object has no attribute 'spltt'. Did you mean: 'split'?
names.split()
['sravani', 'niharika', 'pavithra']
names.split('i')
['sravan', ' n', 'har', 'ka pav', 'thra']
names.rsplit()
['sravani', 'niharika', 'pavithra']
names.rsplit('',5)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    names.rsplit('',5)
ValueError: empty separator
names.rsplit(' ',5)
['sravani', 'niharika', 'pavithra']
names.rsplit(' ',3)
['sravani', 'niharika', 'pavithra']
names.rsplit(' ',1)
['sravani niharika', 'pavithra']
names.partition(' ')
('sravani', ' ', 'niharika pavithra')
'1.python.png'.partition('.')
('1', '.', 'python.png')
l=['sravani niharika pavithra']
\
l=['sravani niharika pavithra']
''.join(l)
'sravani niharika pavithra'
'-'.join(l)
'sravani niharika pavithra'
','.join(l)
'sravani niharika pavithra'
h='       ssssss    ssssssss           '
h.strip()
'ssssss    ssssssss'
h.lstrip()
'ssssss    ssssssss           '
h.rstrip()
'       ssssss    ssssssss'
l=['sravani' ,'niharika','pavithra']
''.join(1)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    ''.join(1)
TypeError: can only join an iterable
''.join(l)
'sravaniniharikapavithra'
'-'.join(l)
'sravani-niharika-pavithra'
'hello'.encode()
b'hello'
b'hello'.decode()
'hello'
text='hello'
text.encode()
b'hello'
b'hello'.decode()
'hello'
'python'.startswith('p)
                    
SyntaxError: unterminated string literal (detected at line 1)
'python'.startswith('p')
                    
True
'python'.endswith('.py')
                    
False
'hhdgj'.isalpha()
                    
True
'123jjnjnk'.isalnum()
                    
True
'sff   1234'.isalnum()
                    
False
s=text.encode()
                    
s.decode()
                    
'hello'
'hdj'.islower()
                    
True
'HGGUH'.isupper()
                    
True
'     '.isspace()
                    
True
'Shiva Charan Abhi Varma'.istitle()
                    
True
'myvar'.isidentifier()
                    
True
'my@@hjjjh'.isidentifier()
                    
False
'3456'.sidecimal()
                    
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    '3456'.sidecimal()
AttributeError: 'str' object has no attribute 'sidecimal'. Did you mean: 'isdecimal'?
'233456'.isdecimal()
                    
True
'187829'.isdigit()
                    
True
'0876543'.isnumeric()
                    
True
l=['bvfjeh',1,12.3,[1,2],(1,2),True,{1:1},{1,2,3},None]
                    
l
                    
['bvfjeh', 1, 12.3, [1, 2], (1, 2), True, {1: 1}, {1, 2, 3}, None]
l=[1,1,1,1,1]
                    
l
                    
[1, 1, 1, 1, 1]
l
                    
[1, 1, 1, 1, 1]
l
                    
[1, 1, 1, 1, 1]
l
                    
[1, 1, 1, 1, 1]

l

l
                    
[1, 1, 1, 1, 1]
a=[1,2,3,4]
                    
a*10
                    
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
b=[2,3,4,6]
                    
a+b
                    
[1, 2, 3, 4, 2, 3, 4, 6]
l=['sravani niharika pavithra']
                    

l
                    
['sravani niharika pavithra']
l[0]
                    
'sravani niharika pavithra'
l[1]
                    
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    l[1]
IndexError: list index out of range
l[2]
                    
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    l[2]
IndexError: list index out of range
l=['sravani',' niharika',' pavithra']
                    
l[0]
                    
'sravani'
l[1]
                    
' niharika'
l[2]
                    
' pavithra'
l[-1]
                    
' pavithra'
l[::-1]
                    
[' pavithra', ' niharika', 'sravani']

l[::2]
                    
['sravani', ' pavithra']
l[-3:-1]
                    
['sravani', ' niharika']
l[:1]
                    
['sravani']
l[:0]
                    
[]
l[::0]
                    
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    l[::0]
ValueError: slice step cannot be zero
l[::1]
                    
['sravani', ' niharika', ' pavithra']
l[0:3:1]
                    
['sravani', ' niharika', ' pavithra']
l[1:3:1]
                    
[' niharika', ' pavithra']
'charan'in l
                    
False
l=list()
                    
l=['sravani',' niharika',' pavithra']
                    
id(1)
                    
140728992463288
l[0]
                    
'sravani'
l[0]=shiva
                    
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    l[0]=shiva
NameError: name 'shiva' is not defined
l[0]='shiva'
                    
l
                    
['shiva', ' niharika', ' pavithra']
id(1)
                    
140728992463288
l.append('shiva')
                    
l
                    
['shiva', ' niharika', ' pavithra', 'shiva']
l.insert(1,'varma')
                    
l
                    
['shiva', 'varma', ' niharika', ' pavithra', 'shiva']
l.extend(['charan','harsha'])
                    
l
                    
['shiva', 'varma', ' niharika', ' pavithra', 'shiva', 'charan', 'harsha']
l.remove('shiva')
                    
l
                    
['varma', ' niharika', ' pavithra', 'shiva', 'charan', 'harsha']
l.pop()
                    
'harsha'
l.pop()
                    
'charan'
del l[0]
                    
l.pop(0)
                    
' niharika'
del l[0]
                    
l
                    
['shiva']
sorted(l)
                    
['shiva']
l=['sravani',' niharika',' pavithra']
                    
sotred(l)
                    
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    sotred(l)
NameError: name 'sotred' is not defined. Did you mean: 'sorted'?
sorted(l)
                    
[' niharika', ' pavithra', 'sravani']
max(l)
                    
'sravani'
min(l)
                    
' niharika'
len(l)
                    
3
l
                    
['sravani', ' niharika', ' pavithra']
l.index('niharika')
                    
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    l.index('niharika')
ValueError: 'niharika' is not in list
l.count('sravani')
                    
1
l.index('n')
                    
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    l.index('n')
ValueError: 'n' is not in list
>>> l
...                     
['sravani', ' niharika', ' pavithra']
>>> l.index('n')
...                     
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    l.index('n')
ValueError: 'n' is not in list
>>> l.reverse()
...                     
>>> l
...                     
[' pavithra', ' niharika', 'sravani']
>>> l.sort()
...                     
>>> l
...                     
[' niharika', ' pavithra', 'sravani']
>>> l=[1,2,3]
...                     
>>> m=l
...                     
>>> m.append(12)
...                     
>>> m
...                     
[1, 2, 3, 12]
>>> n=l.copy()
...                     
>>> n.append(10)
...                     
>>> n
...                     
[1, 2, 3, 12, 10]
>>> l
...                     
[1, 2, 3, 12]
