'''file=open('pfs53.txt','r')
print(file.readline())
file.seek(0)
print(file.readlines())
file.seek(0)
print(file.read())
file.close()'''

#this is the recommended method because it can close the file automatically
'''with open('pfs53.txt','r') as file:
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    print(file.read())'''
#write
'''with open('pfs54.txt','w') as file:
    file.write('sahil')
    file.write('\nravi')
    file.write('\nanish')---it is going to create new file'''

'''with open('pfs53.txt','w') as file:
    file.write('sahil')
    file.write('\nravi')
    file.write('\nanish')---it replaces the data present in 53 with the given names'''

#append
'''with open('pfs53.txt','a') as file:
    file.write('sahil')
    file.write('\nravi')
    file.write('\nanish')'''


with open('pfs53.txt','r+') as file:
    file.write('sahil')
    file.write('\nravi')
    file.write('\nanish')
    file.seek(0)
    print(file.read())
