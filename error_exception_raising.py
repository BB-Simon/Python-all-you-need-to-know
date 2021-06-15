# -----------------------------------
# Errors and Exceptions Raising
# -------------------------------------------
# [1] Exception is a runtime error reporting mechansm
# [2] Exception give you the message to understand the problem
# [3] Trackback give you the line to look for code on this line
# [4] Exception have types (SyntaxtError, IndexError, KeyError Etc...)
# [5] Exception List "https://docs.python.org/3/library/exceptions.html"
# [6] raise keyword used to raise your own exceptions
# -----------------------------------------------------

# x = -10
# if x < 0:
#     raise Exception(f"this number {x} is less than zero")
#     # print('it will not exicute coz of exception')
# else:
#     print('that\'s perfect')

# print('message after condition')

# a = 10
# if type(a) != int:
#     raise ValueError('Only Number Allowed')

# print('message after condition')

# -----------------------------------
# ---Exception Handling
# -------Try | Except | Else | Finally
# -------------------------------------------
# [1] Try => Test The Code for Error
# [2] Except => Handle The Error
# ----------------------------------------------
# [3] Else  => If No Error
# [4] Finally => Run The Code
# -----------------------------------------------------

# num = int(input('Enter your age: '))
# print(num)
# print(type(num))

# try:
#     int(input('Enter your age: '))
# except:
#     print('Bad, this is not an integer')
# else:
#     print('Good, that\'s fine')
# finally:
#     print('Wooow...')


# print(10/0)
# try:
#     print(10/0)
#     # print(x)
# except:
#     print('Can\'t divied')


# try:
#     # print(10/0)
#     # print(x)
#     print(int('simon'))
# except ZeroDivisionError:
#     print('Zero Division Error')
# except NameError:
#     print('name error')
# except ValueError:
#     print('value error')
# except:
#     print('error ocurred')

# -----------------------Practical Example-------------------------
the_file = None
the_tries = 5

while the_tries > 0:
    try:
        print('Enter the file name with abs path: ')
        print('e.g example.txt')
        print(f"{the_tries} Tries Left")
        file_name = input('file name =>: ').strip()
        the_file = open(file_name, 'r')
        print(the_file.read())
        break
    except FileNotFoundError:
        print('file not found')
        the_tries -= 1
    except:
        print('error ocurred')
    finally:
        if the_file is not None: 
            the_file.close()
            print('file closed')
else:
    print('All Tries Done')
