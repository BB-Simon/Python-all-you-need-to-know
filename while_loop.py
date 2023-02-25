# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# a = 0
# while a < len(num):
#     print(f'#{str(a + 1).zfill(4)} => {num[a]}')
#     a +=1
# else:
#     print('Loop has done')
# name = 'Simon'
# i = 0
# while i < len(name):
#     print(f'You are: {name[i].upper()}')
#     i+=1
# else:
#     print('Loop has done')
# -----------------------------
# ----------Bookmarks----------
# -----------------------------

# bookmarks = []
# maxbookmarks = 5
# while maxbookmarks > 0:
#     web = input('Mark Your Favourit Website?').strip().lower()
#     bookmarks.append(f'https://{web}.com')
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

# tries = 5
# main_password = 'simon123'
# input_password = input('Enter Your Password: ')
# while input_password != main_password:
#     tries -= 1
#     if tries > 0:
#         print(
#             f"Wrong Password, { 'Last Chance' if tries == 1 else f'{tries} Chances Left' }")
#         input_password = input('Enter Your Password: ')
#     else:
#         print('Oops...! All Chances Are Finished')
#         break
# else:
#     print('It\'s Done...! Happy Codding')


tries = 3
my_havites = ['coding', 'eating', 'running']
your_input = input('tell me one of my favourite havite if you\'re my best freind: ')

while your_input not in my_havites:
    tries -= 1
    if tries > 0:
        print(
            f"Oops...! {'Last chance' if tries == 1 else f'{tries} chances left'}")
        your_input = input('Try again: ')

    if tries == 0:
        print('Oops! all chances are finished, come back letter')
        break
else:
    print('it\'s awsome, you\'re my best friend')
