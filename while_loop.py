# num = [1, 2, 3, 4, 5, 6]
# a = 0
# while a < len(num):
#     print(f'#{str(a + 1).zfill(2)} => {num[a]}')
#     a +=1
# else:
#     print('Loop has done')

# -----------------------------
# ----------Bookmarks----------
# -----------------------------

# bookmarks = []
# maxbookmarks = 5
# while maxbookmarks > 0:
#     web = input('Mark Your Favourit Website?').strip().lower()
#     bookmarks.append(f'https://{web}')
#     maxbookmarks -= 1
#     print(f'Website added, {maxbookmarks} places left')
#     print(bookmarks)
# else:
#     print('You Can\'t Add Any More...')

# if(len(bookmarks) > 0):
#     bookmarks.sort()
#     index = 0
#     print('List of Your Bookmarks')
#     while index < len(bookmarks):
#         print(bookmarks[index])
#         index += 1

# -----------------------------
# ----------Password Guess----------
# -----------------------------

# tries = 2
# main_password = 'simon123'
# input_password = input('Enter Your Password: ')
# while input_password != main_password:
#     tries -= 1
#     print(
#         f"Wrong Password, { 'Last Chance' if tries == 0 else f'{tries} Chances' } Left")
#     input_password = input('Enter Your Password: ')

#     if tries == 0:
#         print('Oops...! All Chances Are Finished')
#         break
# else:
#     print('It\'s Done...! Happy Codding')


# tries = 3
# my_havites = ['coding', 'eating', 'running']
# your_input = input('tell me on of my fav if you\'re my best freind: ')

# while your_input not in my_havites:
#     tries -= 1
#     print(f"Oops...!,{'Last chance' if tries == 0 else f'{tries} chances'} Left")
#     your_input = input('tell me on of my fav if you\'re my best freind: ')

#     if tries == 0:
#         print('Oops! all chances are finished, come back letter')
#         break
# else:
#     print('it\'s awsome, you\'re my best friend')

