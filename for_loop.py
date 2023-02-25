# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     print(num)

# for number in numbers:
#     if number % 2 == 0:
#         print(f'The number: {number} is even')
#     else:
#         print(f'The number: {number} is ood')

# name = 'simon'
# for letter in name:
#     print(f' [{letter.upper().center(11, "*")}] ')

# full_name = "Simon Kabir"
# for x in full_name:
#     print(f'({x.upper()})')

# my_range = range(1, 51)
# for number in my_range:
#     print(number)

# for x in range(1, 21):
#     print(f'Your Fav Number is: ({x})')

# Dictionary
# skills = {
#     'HTML': '89%',
#     'JS': '79%',
#     'Angular': '93%',
#     'ReactJS': '92%',
#     'VueJS': '79%'
# }
# print(skills['JS'])

# for i in skills:
#     print(f'My Prograss In Lang {i} Is {skills[i]}')


# names = ['Simon', 'Jimon', 'Takmina']
# skills = ['HTML', 'CSS', 'JS']

# for name in names:
#     print(f'{name} And Skill is: ')
#     for skill in skills:
#         print(f' - {skill}')

# names = {
#     'Simon': {
#        'HTML': '80%',
#        'CSS': '83%',
#        'JS': '90%'
#     },
#     'Jimon': {
#        'HTML': '87%',
#        'CSS': '85%',
#        'JS': '91%'
#     },
#     'Takmina': {
#        'HTML': '89%',
#        'CSS': '87%',
#        'JS': '95%'
#     }
# }
# print(names['Simon']['CSS'])

# for name in names:
#     print(f'Skills And Progress For {name} is: ')
#     for skill in names[name]:
#         print(f'{skill} => {names[name][skill]}')


# ----------------------------------
# -------Break, Continue, Pass------
# ----------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for number in numbers:
#     if number == 6:
#         continue
#     print(number)

# for number in numbers:
#     if number == 6:
#         break
#     print(number)

# for number in numbers:
#     if number == 6:
#         pass
#     print(number)

# ------------------------------------
# -------Advance Dictionary Loop------
# ------------------------------------

# skills = {
#     'HTML': '87%',
#     'CSS': '85%',
#     'JS': '91%'
# }

# print(skills.items())

# for skill in skills:
#     print(f'{skill} => {skills[skill]}')

# for skill_key, skill_value in skills.items():
#     print(f'{skill_key} => {skill_value}')

# skills = {
#     'HTML': {
#         'main': '80%',
#         'ejs': '90%'
#     },
#     'CSS': {
#         'main': '85%',
#         'sass': '89%'
#     },
#     'JS': {
#         'main': '91%',
#         'React': '87%'
#     }
# }

# for key, value in skills.items():
#     print(f'{key} =>')
#     for keyLang, valueLang in value.items():
#         print(f'  {keyLang}: {valueLang}')

# for skill_key, skill_value in skills.items():
#     print(f'{skill_key} Progress Is: ')
#     for progress_key, progress_value in skill_value.items():
#         print(f' - {progress_key} => {progress_value}')


# user = {
#     'simon': {
#         'name': "simon",
#         'age': 23
#     },
#     'jimon': {
#         'name': "jimon",
#         'age': 22
#     }
# }
# print(user.items())
# for x, y in user.items():
#     print(f'user => ')
#     for j, z in y.items():
#         print(f'{j}: {z}')


# a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a[5])

# for num in a:
#     print(num)
