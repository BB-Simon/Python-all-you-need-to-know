fname = input('What\'s Your First name? ')
mname = input('What\'s Your Middle name? ')
lname = input('What\'s Your Last name? ')
wifename = input('what\'s your wife\'s name?')

fname = fname.strip().capitalize()
mname = mname.strip().capitalize()
lname = lname.strip().capitalize()
wifename = wifename.strip().capitalize()

print(f'Hello {fname} {mname:.1s} {lname} Happy to see you here!')
print(f'Your wife is {wifename}, and she is so sweet :)')