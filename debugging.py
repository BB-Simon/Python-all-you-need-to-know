my_list = [1, 2, 3, 4, 5, 6]

my_dict = {
    'name': 'Simon',
    'age': 28,
    'country': 'Bangladesh'
}

for num in my_list:
    print(num)

for key, value in my_dict.items():
    print(f'{key} => {value}')


def say_hi():
    print('hi')


say_hi()
