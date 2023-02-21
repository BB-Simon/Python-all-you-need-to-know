# Decorator
# Sometime called meta programming
# Everything in python is object even function
# decorator take a function and add some functionality and return it
# Decorator wrap other functions and enhance thire behaviour
# Decorator is a higher order function (function take function as parameter)

# def myDec(fun):
#     def innerFun():
#         print('Hi')
#         fun()
#         print('How are you?')

#     return innerFun

# def sayName():
#     print('Simon')


# printDec = myDec(sayName)
# printDec()

# @myDec
# def sayName():
#     print('Simon')

# sayName()

# def sayAge():
#     print(23)

# sayAge()

# @myDec
# def sayAge():
#     print(23)


# sayAge()

# ------------------------------------------------------
# -------Decorator function with parameters-----
# ------------------------------------------------------
# def mydec(fun):
#     def innerFun(a, b):
#         if a < 5 and b > 10:
#             print('hi')
#         fun(a, b)
#     return innerFun

# def mydecTwo(fun):
#     def innerFun(a, b):
#         if a > 5 and b < 10:
#             print('hello')
#         fun(a, b)
#     return innerFun


# @mydec
# def sum(a, b):
#     print(a + b)

# sum(2, 12)

# @mydecTwo
# def sum_two(a, b):
#     print(a + b)

# sum_two(6, 9)

# ------------------------------------------------------
# -------Decorator = Practical Speed Test-----
# ------------------------------------------------------
# def myDec(fun):
#     def innerFun(*numbers):
#         for number in numbers:
#             if(number < 0):
#                 print('Oops here is a Zero')
#         fun(*numbers)
#     return innerFun

 
# @myDec
# def sum(a, b, c):
#     print(a+b+c)

# sum(10, 10, -10)


# ------------------
from time import time

# def myDec(fun):
#     def wrapper():
#         start = time()
#         fun()
#         end = time()
#         print(f'function running time is: {end - start}')

#     return wrapper


# @myDec
# def bigLoop():
#     for number in range(1, 2000):
#         print(number)


# bigLoop()
