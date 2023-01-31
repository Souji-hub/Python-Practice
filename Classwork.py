#Print the sum of current no. and the previous no. in the range of 10
sum = 0
for i in range(1,10):
    sum = i + (i-1)
    print(sum)


#Print the characters from a string that are present at an even index no.
str = input('Enter a string: ')
count = len(str)
i=0
while i<count:
    if i%2==0:
        print(str[i])
    i+=1

#Remove the first n characters from a string
string = input('Enter a string:')
n= int(input('Enter no. of characters to remove: ')) 
print(string[n:])

#check if the first and last no. of a list is same
lst =[]
n = int(input('No of elemetns in list: '))
print("Enter the elements: ")
for i in range(0,n):
    elem = int(input())
    lst.append(elem)

tot = len(lst)

if lst[0] == lst[tot-1]:
    print('The first and last numbers are same')
else:
    print("The first and last numbers are not same")

#Count the no of occurance of each letter in the word 'MISSISSIPPI'
#Store count of every letter with the letter in a dictionary
def counter(str):
    m,i,s,p = 0,0,0,0
    n = len(str)
    for l in range (0,n):
        letr = str[l]
        if 'M' in letr:
            m+=1
        elif'I' in letr:
            i+=1
        elif 'S' in letr:
            s+=1
        elif 'P' in letr:
            p+=1
        else:
            break
    dict.update({'M': m, 'I': i, 'S': s, 'P': p})
    print (f'{dict} in {str}')

str = 'MISSISSIPPI'
dict = {}
counter(str)



#Write a function to check whether the no is prime or not

def is_prime(num):
    if num < 2:
        return 'Not Prime'
    for i in range(2, num):
        if num % i == 0:
             return 'Not Prime'
    return 'Prime'

n = int(input('Enter a no: '))
print(is_prime(n))




