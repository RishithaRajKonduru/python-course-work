'''def display():
    global num
    num+=10
    print("inside num:",num)
num=10
display()
print("outside num:",num)'''


'''def courses():
    course='Java'
    print("in the start:",course)
    def change():
        nonlocal course
        course='python'
        print("changed:",course)
    change()
    print("final:",course)
courses()'''


'''s='python'
len=5
print(len)'''


'''def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)'''

'''def display(n):
    if n==11:
        return
    display(n+1)
    print(n)
display(1)'''

'''def display(s,ind):
    if ind==len(s):
        return
    print(s[ind])
    display(s,ind+1)
s='python'
display(s,0)'''

'''def display(s,ind):
    if ind==len(s)+1:
        return
    print(s[:ind])
    display(s,ind+1)
s='python programming'
display(s,1)'''


'''def display(s,ind,w):
    if ind==len(s)-w+1:
        return
    print(s[ind:ind+w])
    display(s,ind+1,w)
s='python programming'
display(s,0,6)'''




    





