


import sys
sys.path.insert(1,'.\test\college.py')
import college as clg

c1 = clg.College('Soujanya','Bhaktapur')
print(f'{c1._collegename}, {c1._name} , {c1._address}')
c1._collegename = 'KEC'
print(c1._collegename)

