# class Hello:
#     name = 'Soujanya'
#     age = 23

# hello = Hello()
# print(hello.name)
# hello.name = 'ravi'
# print(hello.name)

# hello1 = Hello()
# print(hello1.name)

# class Calculation:
#     length = 01.0
#     breadth = 1.0

#     #method to calculate the area
#     def calculate_area(self):
#         print('Area is= ', self.length* self.breadth)
    
# calc = Calculation()
# calc.calculate_area()
# calc.length = 5.5
# calc.breadth = 3.3

# calc.calculate_area()


# calc1 = Calculation()
# calc1.calculate_area()

# #Constructors in python

# class Broadway:
    
#     def __init__(self):
#         print('This is a default constructor')

# brd = Broadway()


# class PythonClass:

#     def __init__(self,name,age):
#         print(name,age)

# pc = PythonClass('My Basic Python Class',10)


# #inheritance

# class Animal:
#     name = ''
#     def __init__(self):
#         print("This is constructor in animal")
#     def eat(self):
#         print('I can eat')

    

# class Dog (Animal):

#     def __init__(self): 
#         super().__init__()
#         print("This is init of dog")

#     def display(self):
#         print('The animal is', self.name)

# dog = Dog()
# # dog.display()
# # dog.name = 'Bhotey'
# dog.eat()
# # dog.display()
# # dog1 = Dog()
# # dog1.name = 'Pug'
# # dog1.display()

##inheritence
# class Polygon:
#     def __init__(self,no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input('Enter side' +str(i+1)+":")) for i in range(self.n)]

#     def dispSides(self):
#         for i in range(self.n):
#             print('Side',i+1,'is',self.sides[i])
            
# class Triangle(Polygon):
#     def __init__(self):
#         Polygon. __init__(self,3)

#     def findArea(self):
#         a,b,c = self.sides
#         s = (a+b+c)/2
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print(f'The area of the triangle is {area}')


# t = Triangle()

# t.inputSides()
# t.dispSides()
# t.findArea()


# class Animals:
#     name = ''

#     def eat(self):
#         print('Time to eat')
    
# class Dogs(Animals):
#     def eat(self):
#         super().eat()
#         print("Time to eat bones")

# husky = Dogs()
# husky.eat()

##Multiple inheritence
# class Mammal:
#     def mammal_info(self):
#         print('Mammal')
    
# class WingedAnimal:
#     def winged_animal_info(self):
#         print('Winged animal')

# class Bat(Mammal, WingedAnimal):
#     pass

# b1 = Bat()

# b1.mammal_info()
# b1.winged_animal_info()


# #str method 
# age = str(40)
# print(age)

# height = str('7ft')
# print(height)

# b= bytes('python', encoding='utf-8')

# print(str(b,encoding='ascii', errors = 'ignore'))

# print(str(b,encoding='ascii', errors = 'strict'))


# #Demonstrating use of special methods

# class SillyClass:
#     def __getitem__(self,key):
#         print('Getting item')
#         return[True,False,True,False]

#     def __pow__(self,other):
#         return 'Python like you mean it'

# silly = SillyClass()
# silly [None]

# x = silly **2
# print(x)

# #operator overloading

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('Initialization')

#     #overload < operator
#     def __lt__(self,other):
#         return self.age < other.age


# p1 = Person('Soujanya', 23)
# p2 = Person ('Subedi', 24)

# print(p1<p2)
# print (p2<p1)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     def __str__(self):
#         return "({0},{1})".format(self.x,self.y)

#     def __add__(self,other):
#         x = self.x + other.x
#         y = self.y + other.y

#         return Point(x,y)

# p1 = Point(1,2)
# p2 = Point(2,3)

# print(p1+p2)

#static method() Syntax, unpythonic

# class Dates:
#     def __init__(self, date):
#         self.date = date
#     def getDate(self):
#         return self.date
#     @staticmethod
#     def toDashDate(date):
#         return date.replace('/','-')
    
    
class College:
    _collegename = 'My college yes'
    
    def __init__ (self,name,address):
        self._name = name
        self._address = address

c1 = College ('Soujanya','Bhaktapur')
print(f'{c1._collegename}, {c1._name} , {c1._address}')
c1._collegename = 'KEC'
print(c1._collegename)


#write a python class to connect to db in different folder, create a model/dictionary of user.
#  INSERT USER DATA TO DATAbase, retrieve the data from database using same user model class

# assign to it and display the op in console