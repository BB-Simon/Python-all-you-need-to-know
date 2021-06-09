age = int(input('Enter You Age: '))
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minites = hours * 60
seconds = minites * 60

print('You Lived For: ')
print(f'{months} Months')
print(f'{weeks:,} Weeks')
print(f'{days:,} Days')
print(f'{hours:,} Hours')
print(f'{minites:,} Minites')
print(f'{seconds:,} Seconds')

