# import random
# print(random)
# print(f'Random Floating Numbers: {random.random()}')


# Show All Function Inside The Module
# import random
# print(dir(random))


# Import One Or Two Function From Module
# from random import *
# from random import randint, random, randrange
# print(f'Random Float Number: {random()}')
# print(f'Random Integer Number: {randint(10, 20)}')

# --------------------------------------
# --------Craete Module-------------
# ---------------------------------------
# import sys
# print(sys.path)

# import module_create
# import module_create as fun

# print(dir(module_create))

# fun.say_hello('Simon')
# fun.sum(10, 10)

# from module_create import say_hello
# say_hello('Simon')

# -------------------------------------------------------
# --------Install Externak Packages-------------
# Module List: https://docs.python.org/3/py-modindex.html
# Packages And Module Directory: https://pypi.org/
# PIP Manual: https://pip.pypa.io/en/stable/reference/pip_install/
# ---------------------------------------


import termcolor
import pyfiglet

# print(pyfiglet.figlet_format('Simon'))
# print(termcolor.colored('Simon', color='yellow'))
print(termcolor.colored(pyfiglet.figlet_format('Simon'), color='blue'))
