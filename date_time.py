# import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Current Time and Date
# print(datetime.datetime.now())
# print(datetime.datetime.now().year)
# print(datetime.datetime.now().month)
# print(datetime.datetime.now().day)


# print(datetime.datetime.min)
# print(datetime.datetime.max)


# Only Ciurrent Time 
# print(datetime.datetime.now().time())
# print(datetime.datetime.now().time().hour)
# print(datetime.datetime.now().time().minute)
# print(datetime.datetime.now().time().second)

# Specific Time
# print(datetime.datetime(1992, 2, 10))
# print(datetime.datetime(1992, 2, 10, 10, 45,  23, 123645))

# birth_Day = datetime.datetime(1992, 2, 10)
# date = datetime.datetime.now()

# my_age = ((date - birth_Day).days) / 365
# print(my_age)

# --------------------
# ---------date formating-----------
# https://www.programiz.com/python-programming/datetime/strftime
# -------------------

import  datetime

my_birthday = datetime.datetime(1992, 2, 10)
# print(my_birthday.strftime('%a'))
# print(my_birthday.strftime('%A'))
# print(my_birthday.strftime('%b'))
# print(my_birthday.strftime('%B'))
# print(my_birthday.strftime('%y'))
# print(my_birthday.strftime('%Y'))

# print(my_birthday.strftime('%a %b %y'))
# print(my_birthday.strftime('%A %B %Y'))
# print(my_birthday.strftime('%A/%B/%Y'))
# print(my_birthday.strftime('%A-%B-%Y'))

# date = datetime.datetime.now()

# age = (date - my_birthday).days / 365
# print(age)








