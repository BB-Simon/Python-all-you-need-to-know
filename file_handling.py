# --------------------------------------------------------------------------------------
# -----------File Handling--------------------------------------------------------------
# "a": append   => Open file for appending values, Create file if not exists.
# "r": read     => [Default Value] Open file for read and give error if file not exists.
# "w": write    => Open file for wrinting, Create file if not exists.
# "x": create   => Craete File, Give error if file exists.
# ---------------------------------------------------------------------------------------
# import os

# print(os.getcwd())
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.abspath(__file__))

# my_file = open('simon.txt')
# print(my_file)
# print(my_file.name)
# print(my_file.mode)
# print(my_file.encoding)

# print(my_file.read())
# print(my_file.read(22))

# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# print(my_file.readlines())
# print(my_file.readlines(50))
# print(type(my_file.readlines()))

# for line in my_file:
#     print(line)
#     if line.startswith('I'):
#         break

# my_file.close()

# --------------------------------
# -----Write and append in file---
# --------------------------------

# my_file = open('test.txt', 'w')
# my_file.write('Hello Simon\n')
# my_file.write('How Are You?')


# my_file = open('test1.txt', 'w')
# my_file.write('Hello World\n' * 20)

# my_list = ['Simon\n', 'Jimon\n', 'Takmina\n']
# my_file = open('test2.txt', 'w')
# my_file.writelines(my_list)

# my_file = open('test2.txt', 'a')
# my_file.write('and who are you\n')

# my_file = open('test2.txt', 'a')
# my_file.truncate(5)

# my_file = open('test2.txt', 'a')
# print(my_file.tell())

# my_file = open('test2.txt', 'r')
# my_file.seek(14)
# print(my_file.read())
