# -----------------
# type()
# All data in python is Object
# -----------------
# print(type(10)) # int => Integer
# print(type(10.5)) # float => Floating point number
# print(type('Simon')) # str => String
# print(type([1, 2, 3])) # list => List
# print(type((1, 2, 3))) # tuple => Tuple
# print(type({"One": 1, "Two": 2})) # dict => Dictionary
# print(type(2 == 2)) # bool => Boolean

# -----------------
# Variables
# Syntex => [variable name] [assignment] [value]
# -----------------
# name = 'Simon' # isngle word => normal
# myName = 'Simon' # two words => camelCase
# my_name = 'Simon' # two words => snake_case

# print(name)
# print(my_name)
# print(myName)

# -----------------
# Source Code: Original code you write it on computer
# Translation: Converting source code into machine language
# Compilation: Translate code before run time
# Run time: Priod app takes to execute commands
# Interpreted: Code translate on the fly during execution
# -----------------

# Reserved keywords
# help('keywords')

# -----------------
# Escape sequence charecters
# \b => back space
# \newline => Escape new line + \
# -----------------

# back space
# print('Hello\bsimon')

# print("Hello \
# simon")

# print("Hello \"Simon\"")
# print("Hello \nSimmon")

# carrige return
# print('123456\rabcd')

# Horizontal tab
# print('Hello\tSimon')

# Charecter's hax value
# print("\x73")


# -----------------
# Concatenation
# -----------------
# name = 'Simon'
# msg = 'Love you'

# print(msg + " " + name)

# -----------------
# String
# -----------------

# name = 'Simon'
# print(name[-5])

# Slicing
# print(name[2:4])

# ---------------------------------
# String Methods
# ----------------------------------
# name = '  Simon  '
# print(len(name))
# print(name.strip())
# print(name.rstrip())
# print(name.lstrip())

# title = 'i love 2d Grafich and 3d technology'
# print(title.title())
# print(title.capitalize())
# print(title.upper())
# print(title.lower())

# num = "102"
# print(num.zfill(5))

# split() rsplit()
# a = 'I Love Python'
# print(a.split())

# center()
# name = 'Simon'
# print(name.center(9, "@"))

# count()
# a = 'I Love Python and Python'
# print(a.count("Python"))

# swapcase()
# a = 'I Love Python'
# b = 'i lOVE pYTHON'
# print(a.swapcase())
# print(b.swapcase())

# startswith() endswith()
# a = 'Love You Simon'
# print(a.startswith('L'))
# print(a.endswith("N"))

# index(substring, start, end)
# a = 'I Love Python'
# print(a.index('P', 0, 8))
# print(a.find('P', 0, 8))

# rjust(width, fill, char) ljust(width, fill, char)
# a = 'I Love Python'
# print(a.rjust(20, '$'))
# print(a.ljust(20, '@'))

# splitlines
# a = ''' I
# Love
# Python'''
# print(a.splitlines())
# b = 'I\nLove\nPython'
# print(b.splitlines())

# expandtabs()
# a = 'I\tLove\tPython'
# print(a.expandtabs(1))


# ----------------------------------------------
# String Methods Return Boolean => True or False
# -----------------------------------------------
# istitle(), isspace()
# a = 'I Am Title 2D'
# b = 'I Am Title 2d'
# print(a.istitle())
# print(b.istitle())
# c = ' '
# d = ''
# print(c.isspace(), d.isspace())
# a = 'i love python'
# b = 'I Love python'
# print(a.islower(), b.islower())
# a = 'simon_kabir'
# b = 'simon--kabir'
# print(a.isidentifier(), b.isidentifier())
# a = 'abcz'
# b = 'abc123'
# print(a.isalpha())
# print(b.isalpha())
# print(a.isalnum(), b.isalnum())

# replace(oldvalue, newvalue)
# a = 'I Love PHP'
# print(a.replace('PHP', 'Python'))
# name = ['Badre', 'Basem', 'Simon']
# print('-'.join(name))
# print(' '.join(name))
# print(','.join(name))
# print(type(','.join(name)))

# ---------------------------------
# String Formatting
# ----------------------------------

# ---------placeholder in Old Way--------------
# name = 'Simon'
# age = 27
# rank = 10
# print('My Name Is: ' + name + 'And My Age Is: ' + age)
# print('My Name Is: %s And My Age Is: %d And My Rank Is: %f' % (name, age, rank))

# n = 'Simon'
# l = 'Python'
# y = 0
# print('My Name Is: %s And I\'m a %s Developer With %d Year Exp' % (n, l, y))

# ---------Control Floating Point Number in old way--------------
# num = 10
# print('My Number Is: %d' % num )
# print('My Number Is: %f' % num )
# print('My Number Is: %.3f' % num )

# --------Trancate String in old way----------
# msg = 'Hello There! I Love You All'
# print('Today\'s Message Is: %s' % msg)
# print('Today\'s Message Is: %.12s' % msg)

# ---------placeholder In New Way--------------
# name = 'Simon'
# age = 27
# rank = 10
# print('My Name Is: {} And My Age Is: {} And My Rank Is: {}'.format(name, age, rank))
# print('My Name Is: {:s} And My Age Is: {:d} And My Rank Is: {:f}'.format(name, age, rank))
# print('My Name Is: {:s} And My Age Is: {:d} And My Rank Is: {:.2f}'.format(name, age, rank))

# --------Trancate String in new way----------
# msg = 'Hello There! I Love You All'
# print('Today\'s Message Is: {}'.format(msg))
# print('Today\'s Message Is: {:.12s}'.format(msg))

# ------Formate Money---------
# myMoney = 523402340223
# print('My Money: {}'.format(myMoney))
# print('My Money: {:d}'.format(myMoney))
# print('My Money: {:_d}'.format(myMoney))
# print('My Money: {:,d}'.format(myMoney))

# Rearrange Items
# a, b, c = 'One', 'Two', 'Three'
# print('Hello {} {} {}'.format(a, b, c))
# print('Hello {1} {2} {0}'.format(a, b, c))
# print('Hello {2} {0} {1}'.format(a, b, c))

# x, y, z = 10, 20, 30
# print('My Numbers: {} {} {}'.format(x, y, z))
# print('My Numbers: {1:d} {0:d} {2:d}'.format(x, y, z))
# print('My Numbers: {2:f} {1:f} {0:f}'.format(x, y, z))
# print('My Numbers: {2:.2f} {1:.3f} {0:.4f}'.format(x, y, z))

# ----------Formate in Version3.6+-----------
# name = 'Simon'
# age = 27
# print('name is: {name} and my age is: {age}')
# print(f'name is: {name} and my age is: {age}')


# ---------------------------------
# -----------Number----------------
# ----------------------------------
# print(float(10))
# print(complex(102))
# print(int(10.00))
# print(int(10+3j))

# ----------Arithmetic Operators-----------------

# print(-30 - 20)
# print(-30 - -10)
# print(2.44 - 10.3)
# print(5 + 10 * 100)
# print((5 + 10) * 100)
# print(100 / 20)
# print(int(100 / 20))
# print(8 % 2)
# print(9 % 5)

# -----------Exponents-----------
# print(3 ** 4)
# print(3 * 3 * 3 * 3)

# Floor Division
# print(100 // 20)
# print(110 // 20)
# print(119 // 20)
# print(120 // 20)


# ---------------------------------
# -----------Lists----------------
# ----------------------------------
# myList = ['Simon', 'Jimon', 27, False, 5.4]
# print(myList)
# print(type(myList[-1]))
# print(type(myList[1:3]))
# print(myList[:3])
# print(myList[2:])
# print(myList[::1])
# print(myList[::2])
# print(myList[::3])
# myList[2] = 28
# myList[-2] = True
# myList[0:3] = ['Takmina', 22, True]
# myList[0:3] = ['Takmina']
# print(myList)
# ---------------------------------
# -----------List's Methods----------------
# ----------------------------------

# append()
# myList = [1, 2, 4, 'we']
# myList.append('hi')
# list2 = [5, 6, 7]
# myList.append(list2)
# print(myList)

# extend()
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# a.extend(b)
# print(a)

# remove()
# a = [1, 2, 3, 4]
# a.remove(2)
# print(a)

# sort()
# a = [90, 23, -12, 2, 3, 4, 43]
# a = ['a', 'A', 's', 'c', 'z', 'Z']
# a.sort(reverse=False)
# a.sort(reverse=True)
# print(a)

# reverse()
# a = ['a', 'A', 's', 1, 32, 90, -23]
# a.reverse()
# print(a)

# clear()
# a = ['a', 'A', 's', 1, 32, 90, -23]
# a.clear()
# print(a)

# copy()
# a = ['a', 'A', 's', 1, 32, 90, -23]
# b = a.copy()
# print(b)

# count()
# a = ['a', 'A', 's', 1, 1, 2, 2, 3, 3, 3, 32, 90, -23]
# print(a.count(3))

# index()
# a = ['a', 'A', 's', 1, 32, 90, -23]
# print(a.index('A'))

# insert()
# a = ['a', 'A', 's', 1, 32, 90, -23]
# a.insert(2, 'SIMON')
# print(a)

# pop()
# a = ['a', 'A', 's', 1, 32, 90, -23]
# print(a.pop(2))

# ----------------------------------
# -----------Tuple------------------
# Tuple is immutable
# ----------------------------------
# a = ('Simon', 'Jimon', 'Takmina')
# b = 'Simon', 'Jimon', 'Takmina'
# print(type(a), type(b))
# print(a, b )
# print(a[0], b[-1] )

# a = (1, 2, 3)
# b = 7, 8, 9
# print(type(a))
# print(type(b))
# c = a + (4, 5, 6) + b
# print(c)

# string = 'SIMON'
# list1 = [1, 2]
# myTuple = ('A', 'B')
# print(string * 3)
# print(list1 * 3)
# print(myTuple * 3)

# ---------Tuple Methods----------
# a = (1, 2, 3, 4, 2, 1, 4m, 6, 8, 0)
# print(a.count(2))
# print(f'the Position of 6 is: {a.index(6)}')

# ----------------------------------
# -----------Set------------------
# ----------------------------------
# my_set = {'Simon', 'Jimon', 'Takmina', 100, True}
# print(my_set)
# my_set.clear()
# print(my_set)

# b = {'Souvo', 'Jannat', 'Nyma'}
# c = {True, 'Badr'}
# print(my_set | b)
# print(my_set.union(b, c))

# my_set.add(50)
# print(my_set)

# a = my_set.copy()
# my_set.add(50)
# print(a)

# my_set.remove(100)
# print(my_set)

# my_set.discard(10)
# print(my_set)

# print(my_set)
# print(my_set.pop())

# b = {'Souvo', 'Jannat', 'Nyma'}
# my_set.update(b)
# print(my_set)

# print('/' * 50)

# a = {1, 2, 3, 4}
# b = {3, 4 , 5, 6}
# print(a - b)
# print(a.difference(b))
# print(a)
# print(a)
# a.difference_update(b)
# print(a)

# Intersection
# a = {1, 2, 3, 4, 'B'}
# b = {3, 4 , 5, 6, 'B'}
# print(a)
# print(a.intersection(b)) #a & b
# print(a)
# print('-' * 50)
# print(a)
# a.intersection_update(b)
# print(a)


# a = {1, 2, 3, 4, 'B'}
# b = {3, 4 , 5, 6, 'B'}
# print(a)
# print(a.symmetric_difference(b)) # a ^ b
# print(a)
# print('-' * 50)
# print(a)
# a.symmetric_difference_update(b)
# print(a)

# a = {1, 2, 3, 4, 'B'}
# b = {1, 2, 3, 4}
# print(a.issuperset(b))
# c = {1, 2, 3, 4, 5, 6}
# print(a.issuperset(c))
# print('-' * 50)
# a = {1, 2, 3, 4, 'B'}
# b = {1, 2, 3, 4}
# print(a.issubset(b))

# a = {1, 2, 3, 4, 'B'}
# b = {5, 6, 7, 8}
# print(a.isdisjoint(b))



