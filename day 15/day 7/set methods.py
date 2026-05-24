Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={1:1,2:4,3:9,4:16,5:25,6:36}
d.keys()
dict_keys([1, 2, 3, 4, 5, 6])
d.values()
dict_values([1, 4, 9, 16, 25, 36])
d.items()
dict_items([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)])
len(d)
6
sorted(d)
[1, 2, 3, 4, 5, 6]
max(d)
6
min(d)
1
d.get(7)
d
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
d.setdefault(7,0)
0
d
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 0}

d.setdefault(6,0)
36
d.setdefault(8,64)
64
d
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 0, 8: 64}
#set
#---------------
#unordered ,mutable,unique elements,
s=set()
s={9,1,2,4,10,12,4567,123,9,23,12,1,1,1,1,1,1,1,2,2,2,2,2}
s
{1, 2, 4, 9, 10, 12, 23, 4567, 123}
s=set()
s.add(1)
s
{1}
s.add(1.1)
s
{1, 1.1}
s.add('string')
s
{'string', 1, 1.1}
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
s.add((1,2,3))
s
{'string', 1, (1, 2, 3), 1.1}
s.add(2+3j))
SyntaxError: unmatched ')'
s.add((2+3j))
s
{1, 1.1, 'string', (1, 2, 3), (2+3j)}
s.add({1,2,3,4})
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s.add({1,2,3,4})
TypeError: unhashable type: 'set'
s.add({1:1,2:1})
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.add({1:1,2:1})
TypeError: unhashable type: 'dict'
s
{1, 1.1, 'string', (1, 2, 3), (2+3j)}
s.add(False)
s
{False, 1, 1.1, 'string', (1, 2, 3), (2+3j)}
s.add(True)
s
{False, 1, 1.1, 'string', (1, 2, 3), (2+3j)}
1 in s
True
2 in s
False
1.1 in s
True
1.2 not in s
True
a={1,2,3,4,5,6}
a
{1, 2, 3, 4, 5, 6}
b={2,3,7,8,9,10}
b
{2, 3, 7, 8, 9, 10}
a | b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a & b
{2, 3}
a - b
{1, 4, 5, 6}
b - a
{8, 9, 10, 7}
a ^ b
{1, 4, 5, 6, 7, 8, 9, 10}
a
{1, 2, 3, 4, 5, 6}
{1,2}<a
True
{1,2,10,11,12}<a
False
(1,2,3,4,5,6,7,8,9}>a
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
{1,2,3,4,5,6,7,8,9}>a
True
{1,2}>a
False

x={1,2}
y={3,4}

x.isdisjoint(y)
True
a.isdisjoint(y)
False
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a.intersection(b)
{2, 3}
a.difference(b)
{1, 4, 5, 6}
sorted(a)
[1, 2, 3, 4, 5, 6]
max(a)
6
min(a)
1
len(a)
6
sum(a)
21
a.add(7)
a.add(80)
a
{80, 1, 2, 3, 4, 5, 6, 7}
a.update({67,89,10})
a
{1, 2, 3, 4, 5, 6, 7, 67, 10, 80, 89}
a.pop()
1
a.pop()
2
a.clear()
a
set()

>>> a.add(True)
>>> a
{True}
>>> 
>>> a=(1,2,3,4,5,6,7,67,10,80,89}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> a={1,2,3,4,5,6,7,67,10,80,89}
>>> a
{1, 2, 3, 4, 5, 6, 7, 67, 10, 80, 89}
>>> a.remove(89)
>>> a
{1, 2, 3, 4, 5, 6, 7, 67, 10, 80}
>>> a.discard(3)
>>> a
{1, 2, 4, 5, 6, 7, 67, 10, 80}
>>> b
{2, 3, 7, 8, 9, 10}
>>> a.intersection_update(b)
>>> a
{2, 10, 7}
>>> b
{2, 3, 7, 8, 9, 10}
>>> b
{2, 3, 7, 8, 9, 10}
>>> c=b
>>> c.add(100)
>>> c
{2, 3, 100, 7, 8, 9, 10}
>>> b
{2, 3, 100, 7, 8, 9, 10}
>>> 
>>> d=b.copy()
>>> d
{2, 3, 100, 7, 8, 9, 10}
>>> d.add(200)
>>> d
{2, 3, 100, 7, 8, 9, 10, 200}
>>> b
{2, 3, 100, 7, 8, 9, 10}
