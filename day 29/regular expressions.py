'''import re
pattern=r'[A-Z]'
text='Python Version 3.13.13'
res=re.match(pattern,text) 
print("Match found" if res else "Not matched")'''


'''import re
pattern=r'[A-Z]'
text='Python Version 3.13.13'
res=re.search(pattern,text)----first occurence.
print(res.group() if res else "Not matched")'''


'''import re
pattern=r'[0-9]{2}'----curly braces for length factor.
text='Python Version 3.13.13'
res=re.findall(pattern,text)
print(res)'''


'''import re
pattern=r'[0-9]{2}'
text='Python Version 3.13.13'
res=re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())'''


'''import re
pattern=r'[0-9]{2}'
text='1234567890'
res=re.fullmatch(pattern,text)
print(res.group() if res else "Not matched")'''


'''import re
pattern=r'[0-9]{10}'
text='Phone no:1234567890'
res=re.sub(pattern,'*********',text)
print(res)'''


'''import re
pattern=r'[aeiouAEIOU]'
text='python programming language'
res=re.sub(pattern,'*',text)
print(res)'''


'''import re
pattern=r'[,-:]'
text='python,pro-gram:mi,nglan-gu-age'
res=re.split(pattern,text)
print(res)'''

import re
pattern=r'h.t'
text='hot hit hat hut h@t h-t h4t heat head'
res=re.findall(pattern,text)
print(res)
