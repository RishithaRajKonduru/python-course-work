Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[1,2,3,4,5]
sum(l)
15
#0 0.0 '' [] () set() False {}
any([1,0.0,'',(),set(),[],{},False])
True
all([1,0.0,'',(),set(),[],{},False])

False
all([1,1.1,3,'dnejdhj',[1,2,3]])
True
tuple
<class 'tuple'>
tuple is ordered,immutable,fixed data,alllow duplicates,heterogeneous
SyntaxError: invalid syntax
t=()
t=tuple()
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t
(1, 2, 3, 4, 5)
t
(1, 2, 3, 4, 5)
t.add(1)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    t.add(1)
AttributeError: 'tuple' object has no attribute 'add'
t.append(1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t.append(1)
AttributeError: 'tuple' object has no attribute 'append'
t=(1,1,1,1)
t
(1, 1, 1, 1)
t=(1,1.8,'python',[1,2,3,4],{1,2,3},{1:1,2:2})

t
(1, 1.8, 'python', [1, 2, 3, 4], {1, 2, 3}, {1: 1, 2: 2})
t.append(12)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    t.append(12)
AttributeError: 'tuple' object has no attribute 'append'
t[3]
[1, 2, 3, 4]
t[3].append(15)
t
(1, 1.8, 'python', [1, 2, 3, 4, 15], {1, 2, 3}, {1: 1, 2: 2})
a=(1,2,4)
x,y,z=a
x
1
y
2
z
4
t=(1,2,3,4)
id(t)
2076047413296
t=t+(5,6)
t
(1, 2, 3, 4, 5, 6)
id(t)
2076047635552
t=('charan','surya','john','lakshmikanth','nageswar','dhanunjay')
t
('charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay')
t+('prince','ravi')
('charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay', 'prince', 'ravi')
t*10
('charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay', 'charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay', 'charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay', 'charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay', 'charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay', 'charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay', 'charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay', 'charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay', 'charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay', 'charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay')
t
('charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay')
t[2]
'john'
t[4]
'nageswar'
t[-2]
'nageswar'
t[-1]
'dhanunjay'
t[0]
'charan'
t[-3]
'lakshmikanth'
t[:3]
('charan', 'surya', 'john')
t[-2:]
('nageswar', 'dhanunjay')
t[::2]
('charan', 'john', 'nageswar')
t[1::]
('surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay')
t[::-1]
('dhanunjay', 'nageswar', 'lakshmikanth', 'john', 'surya', 'charan')
t
('charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay')
t[-1:-4:-1]
('dhanunjay', 'nageswar', 'lakshmikanth')
t
('charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay')
'charan' in t
True
'niharika' not in t
True
'john' in t
True
t
('charan', 'surya', 'john', 'lakshmikanth', 'nageswar', 'dhanunjay')
t=(1,1,1,1,1,2,2,2,3,4,5)
t.count(1)
5
t.count(2)
3
t.count(3)
1
t.index(2)
5
t.index(10)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    t.index(10)
ValueError: tuple.index(x): x not in tuple
max(t)
5
min(t)
1
sorted(t)
[1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 5]
sum(t)
23
len(t)
11
s=[9,8,6,7,1,3,2]
s
[9, 8, 6, 7, 1, 3, 2]
sorted(s)
[1, 2, 3, 6, 7, 8, 9]
s
[9, 8, 6, 7, 1, 3, 2]
s.sort()
s
[1, 2, 3, 6, 7, 8, 9]
#dictionaryy
#key-value pair,mutable,ordered,key:unique,value:duplicates,key:immutable,value:no restrictions.
data={}
typr(data)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    typr(data)
NameError: name 'typr' is not defined. Did you mean: 'type'?
type(data)
<class 'dict'>
data
{}
data={'userid':101,'username':'ravi','skills':['python','java','sql','gpa:8.7]}
                                               
SyntaxError: unterminated string literal (detected at line 1)
data={'userid':101,'username':'ravi','skills':['python','java','sql'],'gpa':8.7]}

  
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
data={'userid':101,'username':'ravi','skills':['python','java','sql'],'gpa':8.7]}
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
data={'userid':101,'username':'ravi','skills':['python','java','sql'],'gpa':8.7}
data
{'userid': 101, 'username': 'ravi', 'skills': ['python', 'java', 'sql'], 'gpa': 8.7}
d={}
d[1]='int'
d[1.1]='float'
d
{1: 'int', 1.1: 'float'}
d['string']='str'
d[[1,2,3,4]]='list'
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    d[[1,2,3,4]]='list'
TypeError: unhashable type: 'list'
d[(1,2,3,4)]='tuple'
d
{1: 'int', 1.1: 'float', 'string': 'str', (1, 2, 3, 4): 'tuple'}
d[{1,2,3}]='set'
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    d[{1,2,3}]='set'
TypeError: unhashable type: 'set'
d[{1:1,2:1}]='dict'
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    d[{1:1,2:1}]='dict'
TypeError: unhashable type: 'dict'
d[False]='bool'
d
{1: 'int', 1.1: 'float', 'string': 'str', (1, 2, 3, 4): 'tuple', False: 'bool'}
d[(2+3j)]='complex'
d
{1: 'int', 1.1: 'float', 'string': 'str', (1, 2, 3, 4): 'tuple', False: 'bool', (2+3j): 'complex'}
data['userid']=102
data
{'userid': 102, 'username': 'ravi', 'skills': ['python', 'java', 'sql'], 'gpa': 8.7}
d={}
type(d)
<class 'dict'>
d=dict(d)
type(d)
<class 'dict'>
data+{1:1}
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    data+{1:1}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
data*2
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    data*2
TypeError: unsupported operand type(s) for *: 'dict' and 'int'
data[::1]
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    data[::1]
KeyError: slice(None, None, 1)
data
{'userid': 102, 'username': 'ravi', 'skills': ['python', 'java', 'sql'], 'gpa': 8.7}
'userid' in data
True
'age' not in data
True
data['userid']
102
data['skills']
['python', 'java', 'sql']
data['gpa']
8.7
data['username']
'ravi'
data
{'userid': 102, 'username': 'ravi', 'skills': ['python', 'java', 'sql'], 'gpa': 8.7}
data['age]
     
SyntaxError: unterminated string literal (detected at line 1)
dat['age']
     
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    dat['age']
NameError: name 'dat' is not defined. Did you mean: 'data'?
data.get('username')
     
'ravi'
data.get('age')
     
data.get('age','age is not present')
     
'age is not present'
data
     
{'userid': 102, 'username': 'ravi', 'skills': ['python', 'java', 'sql'], 'gpa': 8.7}
data['username']
     
'ravi'
id(data)
     
2076052723264
data['username']='sahil'
     
data
     
{'userid': 102, 'username': 'sahil', 'skills': ['python', 'java', 'sql'], 'gpa': 8.7}
id(data)
     
2076052723264
data['gpa']=10
     
data
     
{'userid': 102, 'username': 'sahil', 'skills': ['python', 'java', 'sql'], 'gpa': 10}
data['skills'].append('flask')
     
data
...      
{'userid': 102, 'username': 'sahil', 'skills': ['python', 'java', 'sql', 'flask'], 'gpa': 10}
>>> data['age']=21
...      
>>> data
...      
{'userid': 102, 'username': 'sahil', 'skills': ['python', 'java', 'sql', 'flask'], 'gpa': 10, 'age': 21}
>>> data.update({'phoneno':9876543210,'passsedout':2025})
...      
>>> data
...      
{'userid': 102, 'username': 'sahil', 'skills': ['python', 'java', 'sql', 'flask'], 'gpa': 10, 'age': 21, 'phoneno': 9876543210, 'passsedout': 2025}
>>> data.pop('age')
...      
21
>>> data
...      
{'userid': 102, 'username': 'sahil', 'skills': ['python', 'java', 'sql', 'flask'], 'gpa': 10, 'phoneno': 9876543210, 'passsedout': 2025}
>>> data.popitem()
...      
('passsedout', 2025)
>>> data
...      
{'userid': 102, 'username': 'sahil', 'skills': ['python', 'java', 'sql', 'flask'], 'gpa': 10, 'phoneno': 9876543210}
>>> del data['skills']
...      
>>> data
...      
{'userid': 102, 'username': 'sahil', 'gpa': 10, 'phoneno': 9876543210}
>>> data.clear()
...      
>>> data
...      
{}
