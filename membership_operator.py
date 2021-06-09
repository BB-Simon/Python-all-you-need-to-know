# ----------Membership Operaors--------
# in
# not in
# -------------------

# string
# name = 'Simon'
# print('s' in name)
# print('s' not in name)

# List
# reletives = ['Simon', 'Jimon', 'Takmina']
# print('Takmina' in firnds)
# friends = ['John', 'Smith', 'Keli']

# name = 'Takmina'
# if name in reletives:
#     print(f'{name} Is My reletive')
# elif name in friends:
#     print(f'{name} Is My Friend')
# else:
#     print(f'{name} Are Someone Else')

# ------------------------------------
# ----practical membership------------
# ------------------------------------

admins = ['Simon', 'Jimon', 'Takmina']
name = input('Please Enter Your Name?').strip().capitalize()

if name in admins:
    print(f'Hello {name} welcome back')
    option = input('Delete Or Update Your Name?').strip().capitalize()
    if option == 'Update' or option == 'U':
        newName = input('Please Enter A New Name?')
        admins[admins.index(name)] = newName
        print('Your Name Updated')
        print(admins)
    elif option == 'Delete' or option == 'D':
        admins.remove(name)
        print('Name Deleted')
        print(admins)
    else:
        print('Wrong Selection')

else:
    status = input(
        'You are not admin, add you? Y or N?? ').strip().capitalize()
    if status == 'Yes' or status == 'Y':
        admins.append(name)
        print(f'welcome {name} You Have Been Added As Admin')
        print(admins)
    else:
        print(f'Bey Bey {name}')
