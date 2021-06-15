# ----------------------------------------
# ----Built in Functions Part_1-------
# -----------------------------
# all()
# any()
# bin()
# id()
# -----------------------------

# x = [1, 2, 3, 4, 0]

# if all(x):
#     print('All Are True')
# else:
#     print('At Least One them Is False')

# x = [2, [], 0, 0]

# if any(x):
#     print('At Least One Of The Is True')
# else:
#     print('Not Any Of them Is True')

# print(bin(1001))

# a = 'Simon'
# print(id(a))

# ----------------------------------------
# ----Built in Functions Part_2-------
# -----------------------------
# sum()
# round()
# range()
# print()
# -----------------------------
# a = [10, 20, 30, 40]
# b = []
# print(sum(a))
# print(sum(b))
# print(sum(a, 30))

# print(round(100.451))
# print(round(100.551))
# print(round(100.455, 2))
# print(round(100.556, 2))

# print(list(range(0, 20, 3)))

# print('Hello', 'Simon', 'How', 'Are', 'You?', sep='@')
# print('Hello', 'Simon', 'How', 'Are', 'You?', sep=' | ')

# print('Fisrt Line', end=' Hello ')
# print('Second Linen')

# ----------------------------------------
# ----Built in Functions Part_3-------
# -----------------------------
# abs()
# pow()
# min()
# max()
# slice()
# -----------------------------

# print(abs(10))
# print(abs(-10))
# print(abs(10.22))
# print(abs(-10.22))

# @pow(x, y, z): Equivalent to x**y (with two arguments) or x**y % z (with three arguments
# print(pow(2, 5)) # 2* 2* 2* 2* 2 = 32
# print(2 * 2 * 2 * 2 * 2)
# print(pow(2, 5, 10))  # (2* 2* 2* 2* 2) % 10 = 2

# print(min(10, 23, 4, 0, -23))
# print(max(10, 23, 4, 0))

# @slice(): Create a slice object.  This is used for extended slicing
# a = ['A', 'B', 'C', 'D', 'E']
# print(a[:4])
# print(a[slice(4)])
# print(a[slice(2, 4)])

# ----------------------------------------
# ----Built in Functions Part_4-------
# -----------------------------
# map()
# --------------------------------
# Map Take a Function + Iteration
# Map Called Map Coz It Maps the function On Element
# The function can be a pree definded function or a lambda function
# ----------------------------------------------------------------------

# With Pre difind function

# def formateText(txt):
#     return f' - {txt.strip().capitalize()} - '


# txts = ['sImon', '   JimON', 'TakMiNA  ']

# formateData = map(formateText, txts)
# print(formateData)
# for name in formateData:
#     print(name)

# for name in map(formateText, txts):
#     print(name)

# for name in list(map(formateText, txts)):
#     print(name)


# With Lambda function
# txts = ['sImon', '   JimON', 'TakMiNA  ']
# for name in map(lambda txt: f' - {txt.strip().capitalize()} - ', txts):
#     print(name)

# for name in list(map((lambda txt: f' - {txt.strip().capitalize()} - '), txts)):
#     print(name)


# ----------------------------------------
# ----Built in Functions Part_5-------
# -----------------------------
# filter()
# --------------------------------
# Filter Take a Function + Iteration
# Filter Run A Function On Every Element
# The Function Need To Return Boolean Value
# Filter Out All Elements for Which The Function Return True.
# The function can be a pree definded function or a lambda function
# ----------------------------------------------------------------------

# def checkNumbers(num):
#     if num > 10:
# #         return num

# def checkNumbers(num):
#     return num > 10


# numbers = [1, 2, 3, 20, 10, 33, 5, 6]

# res = filter(checkNumbers, numbers)
# print(res)
# for number in res:
#     print(number)

# def checkNames(name):
#     return name.startswith('S') or name.startswith('J') or name.startswith('T') 


# names = ['Simon', 'Jimon', 'Jannat', 'Takmina', 'tania', 'Souvo', 'Deno', 'Tyba']

# res = filter(checkNames, names)
# for name in res:
#     print(name)



# names = ['Simon', 'Jimon', 'Jannat', 'Takmina',
#          'tania', 'Souvo', 'Deno', 'Tyba', 'Sadik']

# res = filter((lambda name: name.startswith(
#     'S') or name.startswith('J') or name.startswith('T')), names)
# for name in res:
#     print(name)

# ----------------------------------------
# ----Built in Functions Part_6-------
# -----------------------------
# Reduce()
# --------------------------------
# Reduce Take a Function + Iteration
# Reduce Run A Function On First And Second Elements And Give Result 
# Then Run Function On Result And Third Element
# Then Run Function On Result And Fourth Element And So On...
# Till One Element Is Left And This Is The Result of Reduce
# The function can be a Pre-Defined function or a lambda function
# ----------------------------------------------------------------------

# from functools import reduce

# def sumAll(num1, num2):
#     return num1 + num2


# numbers = [10, 20, 30, 40, 50]

# res = reduce(sumAll, numbers) 
# print(res) # ((((10 + 20) + 30) + 40) + 50)


# ----------------------------------------
# ----Built in Functions Part_7-------
# -----------------------------
# enumerate()
# help()
# reversed()
# ----------------------------------------------------------------------

# skills = ['Html', 'CSS', 'JS', 'PHP']

# res = enumerate(skills, 20)

# for counter, skill in res:
#     print(f' {counter} - {skill} ')


# print(help(str))

# for skill in reversed(skills):
#     print(skill)

