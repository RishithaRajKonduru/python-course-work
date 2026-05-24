Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='python'
type(s)
<class 'str'>
s=''
s
''
a='pytyon'
id(a)
2000329575232
fname='abc'
lname='asd'
fname+lname
'abcasd'
fname*5
'abcabcabcabcabc'
'2'*10
'2222222222'
names='niharika rishitha sailajaa abhiram venkataram'
names[0]
'n'
names[5]
'i'
names[8]
' '
names[-1]
'm'
names[-9]
'e'
names[0"8:1]
      
SyntaxError: unterminated string literal (detected at line 1)
names=[0:8:1]
      
SyntaxError: invalid syntax

names[:8]
      
'niharika'
names[9:17]
      
'rishitha'
names=[18:26]
      
SyntaxError: invalid syntax
names=[18:27]
      
SyntaxError: invalid syntax
names[18:26]
      
'sailajaa'
names[::-1]
      
'marataknev marihba aajalias ahtihsir akirahin'
names[-1:-8:-1]
      
'maratak'
names[::2]
      
'nhrk ihtasiaa bia ektrm'
names[ 29:34]]
SyntaxError: unmatched ']'
names[29:34]
'hiram'
names[26:34]
' abhiram'
names[35:44]
'venkatara'
names[35:45]
'venkataram'
names[:34]
'niharika rishitha sailajaa abhiram'
names[-1:-35:-1]
'marataknev marihba aajalias ahtihs'
rishitha in names
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    rishitha in names
NameError: name 'rishitha' is not defined
'rishitha' in names
True
'shiva' not in names
True
'charan' in names
False
chr(255)
'ÿ'
chr(200)
'È'
chr(20)
'\x14'
chr(50)
'2'
len(names)
45
ord(a)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    ord(a)
TypeError: ord() expected a character, but string of length 6 found
ord('a')
97
ord('0')
48
sorted(names)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'e', 'h', 'h', 'h', 'h', 'i', 'i', 'i', 'i', 'i', 'i', 'j', 'k', 'k', 'l', 'm', 'm', 'n', 'n', 'r', 'r', 'r', 'r', 's', 's', 't', 't', 'v']
char(99)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    char(99)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr('99)
    
SyntaxError: unterminated string literal (detected at line 1)
chr('99')
    
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    chr('99')
TypeError: 'str' object cannot be interpreted as an integer
chr(99)
    
'c'
chr(255)
    
'ÿ'
max(names)
    
'v'
min(names)
    
' '
names.upper()
    
'NIHARIKA RISHITHA SAILAJAA ABHIRAM VENKATARAM'
nmes.lower()
    
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    nmes.lower()
NameError: name 'nmes' is not defined. Did you mean: 'names'?
names.lower()
    
'niharika rishitha sailajaa abhiram venkataram'
l='rishitha sailajaa abhiram venkataram'
    
l.capitalize()
    
'Rishitha sailajaa abhiram venkataram'
l.title()
    
'Rishitha Sailajaa Abhiram Venkataram'
names.swapcase()
    
'NIHARIKA RISHITHA SAILAJAA ABHIRAM VENKATARAM'
names='Rishita Sailaja Venkataram Abhiram'
    
names.swapcase()
    
'rISHITA sAILAJA vENKATARAM aBHIRAM'
"ejyrhwjdhejwieuioeqihoi".casefold()
    
'ejyrhwjdhejwieuioeqihoi'
names.center(40,'-')
    
'---Rishita Sailaja Venkataram Abhiram---'
names.center(30,'*')
    
'Rishita Sailaja Venkataram Abhiram'
names.center(50.'*')
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
names(50,'*')
    
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    names(50,'*')
TypeError: 'str' object is not callable
names.center(40,'*')
    
'***Rishita Sailaja Venkataram Abhiram***'
names.ljust(30,'-')
    
'Rishita Sailaja Venkataram Abhiram'
names.rjust(50,'-')
    
'----------------Rishita Sailaja Venkataram Abhiram'
names.ljust(60,'-')
    
'Rishita Sailaja Venkataram Abhiram--------------------------'
'66'.zfill(6)
    
'000066'
names
    
'Rishita Sailaja Venkataram Abhiram'
names.find('n')
    
18
names.find('z')
    
-1
names.rfind('i')
    
30
names.rfind('a')
    
32
names.find('s')
    
2
names.index('a')
    
6
names.rindex('a')
    
32
names.index('z')
    
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    names.index('z')
ValueError: substring not found
names.count('a')
    
8
names.count('i')
...     
4
>>> names.count('z')
...     
0
>>> names.count('c')
...     
0
>>> names
...     
'Rishita Sailaja Venkataram Abhiram'
>>> names.replace('a','1')
...     
'Rishit1 S1il1j1 Venk1t1r1m Abhir1m'
>>> names.repalce('i','0')
...     
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    names.repalce('i','0')
AttributeError: 'str' object has no attribute 'repalce'. Did you mean: 'replace'?
>>> names.replace('i','0')
...     
'R0sh0ta Sa0laja Venkataram Abh0ram'
>>> names.replace('Rishitha','')
...     
'Rishita Sailaja Venkataram Abhiram'
>>> names.replace('Rishitha',' ')
...     
'Rishita Sailaja Venkataram Abhiram'
>>> names.replace('Rishita','')
...     
' Sailaja Venkataram Abhiram'
>>> names.maketrans('aeiou','12345')
...     
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
>>> names.translate(names.maketrans('aeiou','12345'))
...     
'R3sh3t1 S13l1j1 V2nk1t1r1m Abh3r1m'
