# Generators
# generator is a function with "yield" keyword instead of return keyword
# it supports iteration and return generator iterator by calling 'yield'
# it can have one or more 'yield' 
# by using next() it resums from where it called 'yield' not from begining
# when it called, it not start automatically, it only gives you the controll

# def myGenerator():
#     return 2
# print(myGenerator())


def myGenerator():
    yield 1
    yield 2
    yield 3


# print(myGenerator())
# print(type(myGenerator()))

gen = myGenerator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# print(next(gen))
# print('Hi')
# print(next(gen))
# print('Hello')
# print(next(gen))

print(next(gen))
print('Hi')
print(next(gen))

print("*" * 30)

for num in gen:
    print(num)

print("*" * 30)
for num in myGenerator():
    print(num)
