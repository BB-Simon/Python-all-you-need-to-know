# ---------------------------------------
# -----------Dictionary------------------
# ---------------------------------------
# user = {
#     'name': 'Simon',
#     'age': 28,
#     'country': 'Bangladesh'
# }

# print(user['name'])
# print(user.get('country'))
# print(user.keys())
# print(user.values())

# user = {
#     'Simon': {
#         'name': 'Simon',
#         'age': 28,
#         'country': 'Bangladesh'
#     },
#     'John': {
#         'name': 'John',
#         'age': 26,
#         'country': 'UK'
#     },
#     'Sara': {
#         'name': 'Sara',
#         'age': 23,
#         'country': 'Egypt'
#     }
# }

# print(user.keys())
# print(user['Simon']['country'])
# print(user['Simon'].keys())
# print(user['Simon'].values())

# -----------------------------------------------
# -----------Dictionary Methods------------------
# -----------------------------------------------
# a = {
#     'name': 'Simon'
# }
# print(a)
# a.clear()
# print(a)
# a['age'] = 28
# a.update({'score': 88.5})
# print(a)

# print('-'*50)
# b = a.copy()
# print(b)

# a = {
#     'name': 'Simon',
#     'lname': 'Kabir'
# }
# print(a)
# print(a.setdefault('fname', 'Jimon'))
# print(a.setdefault('age', 27))
# print(a)
# print(a.popitem())
# print(a)

# items = a.items()
# a['age'] = 28
# print(items)

# a = ('name',)
# b = ('Simon', 28, 'Bangladesh')

# c = dict.fromkeys(a, b)
# print(c)
