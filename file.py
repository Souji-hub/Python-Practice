#read
with open('hello.txt','r') as reader:
    print(reader.read())

with open('hello.txt', 'r') as reader:
    print(reader.readline(10))

my_file = open("hello.txt", 'r')
f = my_file. readlines()
print(list(f))

#write
new_file = open('new_file.txt', mode= 'w', encoding = 'utf-8')
new_file.write('this is just an imaginary txt i intend to write. ')
new_file.close()

#append
fruits = ['Orange ',
'banana ',
'apple ',
'pineapple ']

new_file = open('new_file.txt', mode = 'a+', encoding='utf-8')
new_file.writelines(fruits)
new_file.close()

with open ('new_file.txt', 'r') as reader:
        print(reader.read())

#seek
new_file= open('new_file.txt', 'r')
new_file.seek(15)
print(new_file.readlines())

#format
x = 'looked'
y = 10
print('Ram %s and %s before he %s'%(x,'walked',x))
print('please give me my %d rupees'%y)

import os
# file name with extension
file_name = os.path.basename('./new_file.txt')

#file name without extension and with extension
print(os.path.splitext(file_name)[0])
print(os.path.splitext(file_name)[1])

#file_object
with open('new_file.txt','r') as file_obj:
        contents = file_obj.read()
        print(contents)
        
#catching file exceptions 

filename = 'hi.txt'
try:
    with open('hi.txt','r') as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    msg = 'Sorry the file %s does not exist'%filename
    print(msg)

#modules..............###

import sampleModule as sm
sm.greetings('Soujanya')

person = sm.person1['age']
print(person)

import platform
x = platform.system()
print(x)    