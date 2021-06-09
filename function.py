# def sayHi():
#     return 'Hi Simon'
# greeting = sayHi()

# print(greeting)

# a, b, c = 'Simon', 'Jimon', 'Takmina'


# def say_Hello(name):
#     print(f'Hello {name}')


# say_Hello(a)
# say_Hello(b)
# say_Hello(c)

# def add(x, y):
#     if type(x) != int or type(y) != int:
#         print('Only Number Allowed')
#     else:
#         print(x + y)


# add(-50, 100)

# def full_name(fname, mname, lname):
#     print(f'Hello {fname.strip().capitalize()} {mname.upper():.1s} {lname}')


# full_name('   badre   ', 'Basem', 'Simon')


# ---------------------------------------
# ------Packing, Unpacking Parameters----
# ---------------------------------------

# the Problem
# def hello(a, b, c):
#     names = [a, b, c]
#     for name in names:
#         print(f'Hello {name}')

# hello('Simon', 'Jimon', 'Takmina', 'Souvo')

# The Solution
# def hello(*names):
#     for name in names:
#         print(f'Hello {name}')


# hello('Simon', 'Jimon', 'Takmina', 'Souvo', 'Jannat', 'Tyba')


# def my_skill(name, *skills):
#     print(f'Hello {name}! Your Skills Are: ')
#     for skill in skills:
#         print(f' - {skill}')

# my_skill('Simon', 'Html', 'CSS', 'JS', 'Python')
# my_skill('Jimon', 'Html', 'CSS', 'JS', 'Python', 'Data Sience')


# ---------------------------------------
# ------Default Parameters---------------
# ---------------------------------------

# def say_hello(name='Unknown', age='Unknown', country='Unknown'):
#     print(f'Hello {name}, your age is: {age} and you are from {country}')


# say_hello('Simon', 28, 'Bangladesh')
# say_hello()

# -------------------------------------------------
# ------Packing, Unpacking Arguments **KWArgs------
# -------------------------------------------------

# def show_skills(*skills):
#     print(type(skills))
#     for skill in skills:
#         print(f' - {skill}')

# show_skills('JS', 'CSS', 'Go')

# def show_skills(**skills):
#     print(type(skills))
#     for skill, value in skills.items():
#         print(f' - {skill} => {value}')


# show_skills(JS = '80%', CSS = '89%', Go = '56%')

# my_skills = {
#     'JS': '98%',
#     'css': '99%',
#     'Go': '76%'
# }


# def show_skills(**skills):  # show_skills() takes 0 positional arguments but 1 was given
#     print(type(skills))
#     for skill, value in skills.items():
#         print(f' - {skill} => {value}')


# show_skills(my_skills)

# def show_skills(**skills):
#     print(type(skills))
#     for skill, value in skills.items():
#         print(f' - {skill} => {value}')


# show_skills(**my_skills)


# --------------------------------------------------
# ------Packing, Unpacking Arguments Training-------
# --------------------------------------------------

# myTuple = ('Html', 'CSS', 'JS')
# myDict = {
#     'Go': '76%',
#     'Python': '87%',
#     'NodeJS': '78%'
# }


# def show_skills(name, *my_tuple, **my_dict):

#     print(type(my_tuple))
#     print(type(my_dict))

#     print(f'Hello {name}\nYour Skills Without Progress is: ')
#     for skill in my_tuple:
#         print(f' - {skill}')
#     print('Your Skills With Progress is: ')
#     for skill_key, skill_value in my_dict.items():
#         print(f' - {skill_key} => {skill_value}')


# show_skills('Simon', *myTuple, **myDict)


# --------------------------------------------------
# ------Function Scope-------
# --------------------------------------------------

# x = 1 # Global Scope

# def One():
#     print(f'X called within function from  global Scope {x}')

# print(f'X from global scope {x}')
# One()


# def One():
# global x
#     x = 2
#     print(f'X from function Scope {x}')


# print(f'X from global scope {x}')
# One()

# def Two():
#     x = 4
#     print(f'X functional Scope {x}')


# print(f'X from global scope {x}')
# Two()


# --------------------------------------------------
# -----------Recursion Function -------------------
# --------------------------------------------------

# Test Word [wwwooorrrldd]
# x = 'wwwooorr
# rldd'
# print(x[1:])
# print(len(x))

# def cleen_word(word):
#     if len(word) == 1:
#         return word
#     print(f'Before function start: {word}')
#     if word[0] == word[1]:
#         print(f'Before condition: {word}')
#         return cleen_word(word[1:])

#     print(f'Before Return: {word}')
#     print(f'Index Zero Before Return: {word[0]}')
#     return word[0] + cleen_word(word[1:])


# print(cleen_word('wwwooorrrldd'))


# --------------------------------------------------
# -----------Function => Lambda -------------------
# -----------Anonymous Function -------------------
# Lambda is one single expression not block of code
# --------------------------------------------------

# def say_Hello(name):
#     return f'Hello {name}'


# print(say_Hello('Simon'))

def say_Hello(name, age): return f'Hello {name}, And Your Age Is: {age}'
print(say_Hello('Simon', 28))
print(say_Hello.__name__)
print(type(say_Hello))

print('-' * 30)

hello = lambda name, age : f'Hello {name} And Your Age Is: {age}'
print(hello('Simon', 28))
print(hello.__name__)
print(type(hello))
