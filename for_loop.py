# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     if number % 2 == 0:
#         print(f'The number: {number} is even')
#     else:
#         print(f'The number: {number} is ood')

# name = 'simon'
# for letter in name:
#     print(f' [ {letter.upper()} ] ')

# my_range = range(1, 51)
# for number in my_range:
#     print(number)

# Dictionary
# skills = {
#     'HTML': '89%',
#     'JS': '79%',
#     'Angular': '93%',
#     'ReactJS': '92%',
#     'VueJS': '79%'
# }
# for skill in skills:
# print(skill)
# print(f'My Prograss In Lang {skill} Is {skills[skill]}')


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
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
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

# for skill_key, skill_value in skills.items():
#     print(f'{skill_key} Progress Is: ')
#     for progress_key, progress_value in skill_value.items():
#         print(f' - {progress_key} => {progress_value}')


# a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a[5])

# for num in a:
#     print(num)
