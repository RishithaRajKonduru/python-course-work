#system module
'''import sys
print(sys.argv)
print()
print(sys.path)
print()
print(sys.version)
sys.exit()
print("End")'''

#platform
'''import platform
print(platform.system())--os name
print(platform.release())--os release version
print(platform.processor())--processor type'''


'''import math
print(math.e)
print(math.sqrt(16))
print(math.pow(2,3))
print(math.ceil(-12.00000001))
print(math.ceil(-12.3))
print(math.ceil(-12.6))
print(math.ceil(-12.99999))
print(math.floor(-12.000000001))
print(math.floor(-12.3))
print(math.floor(-12.6))
print(math.floor(-12.99999999))'''


'''import math
print(math.fabs(-123))
print(math.factorial(6))
print(math.gcd(44,12))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(190))
print(math.radians(190))'''

#random module
'''import random
print(random.random())
print(random.randint(1,3))
print(random.uniform(1,3))
l=['python','java','c++','c','html']
print(random.choice(l))
print(random.choices(l,k=2))
print("Before:",l)
random.shuffle(l)
print("After:",l)'''


'''import collections
s='python programming'
#s=[1,2,3,5,6,1,2,3,4,2,1,1,1,1,2,3,4]
d=collections.defaultdict(int)
for i in s:
    d[i]+=1
print(d)


d=collections.deque([])
d.append(10)
d.append(20)
d.popleft()
d.append(30)
d.popleft()
d.popleft()
d.append(40)
d.append(50)
print(d)'''

'''from itertools import combinations,permutations
print(list(combinations('ABCD',3)))
print(list(permutations('ABCD',3)))'''



