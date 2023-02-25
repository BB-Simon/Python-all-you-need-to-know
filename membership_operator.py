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
# friends = ['John', 'Smith', 'Keli']
# print('Takmina' in reletives)
# print('Takmina' not in friends)
# print('Takmina' in friends)

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

# admins = ['Simon', 'Jimon', 'Takmina']
# name = input('Please Enter Your Name?').strip().capitalize()

# if name in admins:
#     print(f'Hello {name} welcome back')
#     option = input('Delete Or Update Your Name?').strip().capitalize()
#     if option == 'Update' or option == 'U':
#         newName = input('Please Enter A New Name?')
#         admins[admins.index(name)] = newName
#         print('Your Name Updated')
#         print(admins)
#     elif option == 'Delete' or option == 'D':
#         admins.remove(name)
#         print('Name Deleted')
#         print(admins)
#     else:
#         print('Wrong Selection')
# else:
#     status = input(
#         'You are not admin, add you? Y or N?? ').strip().capitalize()
#     if status == 'Yes' or status == 'Y':
#         admins.append(name)
#         print(f'welcome {name} You Have Been Added As Admin')
#         print(admins)
#     else:
#         print(f'Bey Bey {name}')



flowers = ['Smith', 'Jonh', 'Hasan']
name = input('Enter your name to check are you my flower: ').strip().capitalize()

if name in flowers:
    print(f'Welcome {name}, you\'re flowing me')
    option = input('Unflow me or Edit your name? Press U or E: ').strip().capitalize()
    if option == 'Edit' or option =='E':
        newName = input('Please enter a new name').strip().capitalize()
        flowers[flowers.index(name)] = newName
        print('Your name updated')
        print(flowers)
    elif option == 'Unflow' or option == 'U':
        flowers.remove(name)
        print('You have unflowed me')
        print(flowers)
    else:
        print('Wrong Selection')
else:
    status = input('Would want to flow me? Press Y: ').strip().capitalize()
    if status == 'Yes' or status == 'Y':
        flowers.append(name)
        print(f'Welcome {name} from now you\'re my flower')
        print(flowers)
    else:
        print(f'Good bey {name}')

  