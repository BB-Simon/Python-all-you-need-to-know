# -----------------------------------
# DocString & Commenting vs Documentation
# -------------------------------------------
# [1] Documentation String for class, module, or functions
# [2] Can be access from doc and help attributes
# [3] Made from understading of functionality of complex code
# [4] There One and Multiple line Doc String
# -----------------------------------------------------

def sayHello(name):
    # '''This is a function to say hello'''
    """
    funtion:
        sayHello
    params:
        name => visitor name
    return:
        hello message
    """
    print(f'Hello {name}')


# sayHello('Simon')
# print(sayHello.__doc__)
# help(sayHello)

