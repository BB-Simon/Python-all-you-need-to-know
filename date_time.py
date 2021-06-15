import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Current Time and Date
# date = datetime.datetime
# print(date.now())
# print(date.now().year)
# print(date.now().month)
# print(date.now().day)

# print(date.min)
# print(date.max)

# Only Ciurrent Time 
# print(date.now().time())
# print(date.now().time().hour)
# print(date.now().time().minute)
# print(date.now().time().second)

# Specific Time
# print(date(1992, 2, 10))
# print(date(1992, 2, 10, 10, 45,  23, 123645))

# birth_Day = date(1992, 2, 10)
# date = datetime.datetime.now()
# my_age = ((date - birth_Day).days) / 365
# print(my_age)

# --------------------
# ---------date formating-----------
# https://www.programiz.com/python-programming/datetime/strftime
# -------------------

# my_birthday = datetime.datetime(1992, 2, 10)
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








