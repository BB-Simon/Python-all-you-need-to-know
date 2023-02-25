print('-'*110)
print('You Can Write the fisrt letter or full name of the time unit'.center(110, '-'))
print('-'*110)
# Collect age data
age = int(input('Enter Your age: ').strip())
# Collect Time Unit data
unit = input('Please Select Your Time Unit: Months, Weeks, Days: ').strip().lower()

# Get Time Units
months = age * 12
weeks = months * 4
days = age * 365

if unit == 'months' or unit == 'm':
    print('You Select Months')
    print(f'You Lived For: {months:,} Months')
elif unit == 'weeks' or unit == 'w':
    print('You Select Weeks')
    print(f'You Lived For: {weeks:,} Weeks')
elif unit == 'days' or unit == 'd':
    print('You Select Days')
    print(f'You Lived For: {days:_} Days')
else:
    print('You selected something from out the box')
