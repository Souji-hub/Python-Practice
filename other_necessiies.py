# def AddMethod():
#     return 5+5

# let = AddMethod
# print(callable(let))

# num = 5*5 
# print(callable(num))


# class Check:
#     def __call__(self):
#         print('hello call check method')

# print(callable(Check))

# object = Check()
# object()

# class Noncallable:
#     def testFunc(self):
#         print('Hello test func non callable')
    
# print(callable(Noncallable))
# object1 = Noncallable()
# print(callable(object1))
# object1.testFunc()


# def plus_two(number):
#     def add_two(number):
#         return number + 2
    
#     result = add_two(number)
#     return result

# print(plus_two(5)) 

# def hello_function():
#     def say_hi():
#         return "Hi"
#     return say_hi
# hello = hello_function()
# print(hello())


# def print_message(message):
#     'Enclosing function'
#     def message_sender():
#         'Nester Function'
#         print(message)

#     message_sender()
# print_message("Some random message")

# # //////////////////////////////////////////////
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase =  func.upper()
#         return make_uppercase

#     return wrapper

# def say_hi():
#     return 'hello there'

# decorate = uppercase_decorator(say_hi)
# print(decorate())

# @uppercase_decorator
# def say_hello():
#     return 'hello there'

# # /////////////////////////////////////////////////////////////
# def decorator_with_arguements(function):
#     def wrapper_accepting_arguments(arg1,arg2):
#         print("My arguments are: {0}, {1}".format(arg1,arg2))
#         function(arg1,arg2)
#     return wrapper_accepting_arguments

# @decorator_with_arguements
# def cities(city_one,city_two):
#     print('cities I love are {0} and {1}'.format(city_one,city_two))

# cities("nairobi","accra")

# /////////////////////////////////////////////////////////////////
def a_decorator_pass_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_pass_arbitrary_arguments
def function_with_no_arguments():
    print('No arguments here')

function_with_no_arguments()

@a_decorator_pass_arbitrary_arguments
def function_with_arguments(a,b,c):
    print(a,b,c)

function_with_arguments(1,2,3)

@a_decorator_pass_arbitrary_arguments
def function_with_kwarg():
    print('This has shown keyword arguments')

function_with_kwarg(first_name= 'Soujanya', last_name = 'Subedi')



