fname = input('What\'s Your First name? ')
mname = input('What\'s Your Middle name? ')
lname = input('What\'s Your Last name? ')

fname = fname.strip().capitalize()
mname = mname.strip().capitalize()
lname = lname.strip().capitalize()

print(f'Hello {fname} {mname:.1s} {lname} Happy to see you here!')
