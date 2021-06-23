# ---------------------------------------------------------------
# -- OPP-Part-2 => Class Syntext and info
# ---------------------------------------------------------------
# [1] Class is the Blueprint or constructor of the object
# [2] Class instansiate means create instance of a class
# [3] Instance => Object created from a class and has it's methods and attributes
# [4] Class define with keyword 'class'
# [5] Class name writen in PascalCase [UpperCamelCase] style
# [6] Class may contains methods and attributes
# [7] when creating object python looks for the built in '__init__'method
# [8] __init__ method called every time you create object from class
# [9] __init__ initialize the data for the object
# [10] any method with two underscore in the start and end called dunder or magic method
# [11] 'self' refer to the current instance created from the class and must be first param
# [12] 'self' can be named anything
# [13] in python you do not need to call new() to create object
# ----------------------------------------------------------------------

# class Member:
#     def __init__(self):
#         print('new member added')

# m_one = Member()
# m_two = Member()
# print(m_one.__class__)

# class SayHello:
#     def __init__(self):
#         print('Hello World!')

# hello = SayHello()

# ----------------------------------------------
# --OPP-Part-2-3 => Instance Attributes and Methods
# --------------------------------------------------
# 'self' points to the instance created from class
# Instance Attributes => it's defined inside the constructor
# --------------------------------------------------
# Instance Method => takse 'self' as a param wich points to the instance created from class
# Instance Method => it can have more than One param like any function
# Instance Method => can freely access attributes and methods on the same Object
# Instance Method => can access the class it's self
# --------------------------------------------------

# class Member:
#     def __init__(self, f_name, m_name, l_name, gender):
#         self.f_name = f_name
#         self.m_name = m_name
#         self.l_name = l_name
#         self.gender = gender

#     def full_name(self):
#         return f"{self.f_name} {self.m_name} {self.l_name}"

#     def sayHello(self):
#         if self.gender == 'Male':
#             return f"Hello Mr. {self.f_name}"
#         elif self.gender == 'Female':
#             return f"Hello Miss. {self.f_name}"
#         else:
#             return f"Hello {self.f_name}"

#     def get_all_info(self):
#         return f"{self.sayHello()}, Your full name is: {self.full_name()}"


# member_one = Member('Badre', 'Basem', 'Simon', 'Male')
# member_two = Member('Takmina', 'Aktar', 'Idon', 'Female')

# print(member_one.f_name, member_one.m_name, member_one.l_name)
# print(member_one.full_name())
# print(member_two.sayHello())
# print(member_one.sayHello())
# print(member_one.get_all_info())

# class Person:
#     def __init__(self, first_name, last_name, age, email, isMaried):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.email = email
#         self.isMaried = isMaried
#     def sey_hi(self):
#         return f'Hello {self.first_name}'

#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'

#     def get_all_info(self):
#         return f'Name: {self.first_name} {self.last_name} \n Age: {self.age} \n Email: {self.email} \n IsMaried: {self.isMaried}'


# person1 = Person('simon', 'Kabir', 29, 'test@email.com', False)
# print(person1.get_all_info())
# print(person1.get_full_name())

# ---------------------------------------------
# OOP-Part-4 => Class Attribute
# --------------------------------------------------
# Class Attribute => Attributes defined outside constructor
# ----------------------------------------------------------


# class Member:
#     not_allowed_names = ['shit', 'fuck', 'demn']
#     user_count = 0

#     def __init__(self, f_name, m_name, l_name, gender):
#         self.f_name = f_name
#         self.m_name = m_name
#         self.l_name = l_name
#         self.gender = gender
#         Member.user_count += 1

#     def full_name(self):
#         if self.f_name in Member.not_allowed_names:
#             raise ValueError('this name in not allowed')
#         else:
#             return f"{self.f_name} {self.m_name} {self.l_name}"

#     def sayHello(self):
#         if self.gender == 'Male':
#             return f"Hello Mr. {self.f_name}"
#         elif self.gender == 'Female':
#             return f"Hello Miss. {self.f_name}"
#         else:
#             return f"Hello {self.f_name}"

#     def get_all_info(self):
#         return f"{self.sayHello()}, Your full name is: {self.full_name()}"

#     def delete_user(self):
#         Member.user_count -= 1
#         return f"user {self.f_name} is deleted"

# # print(Member.user_count)
# member_one = Member('Badre', 'Basem', 'Simon', 'Male')
# member_two = Member('Takmina', 'Aktar', 'Idon', 'Female')
# member_three = Member('shit', 'fuck', 'demn', 'dd')
# print(Member.user_count)
# print(member_three.delete_user())
# print(Member.user_count)

# print(member_three.get_all_info())


# ------------------------------------------------------
# --OOP Part-6 => class method and static methods
# ---------------------------------------------------
# Class Methods =>
# --Marked with @classmethod decorator to flag it's class method
# --it takes cls param not 'self' to point to the class not to the instance
# --it doesn't require creation of class instance
# --used when you want to  do something with class itself
# Static Methods =>
# --it takes no params
# --it bounds to the class not instance
# --used when doing something doesn't have access to object or class but releted to class
# ---------------------------------------------------------
# class Member:
#     not_allowed_names = ['shit', 'fuck', 'demn']
#     user_count = 0

#     @classmethod
#     def show_user_count(cls):
#         print(f"user count: {cls.user_count}")

#     @staticmethod
#     def say_hi():
#         print('Hi from Static method')

#     def __init__(self, f_name, m_name, l_name, gender):
#         self.f_name = f_name
#         self.m_name = m_name
#         self.l_name = l_name
#         self.gender = gender
#         Member.user_count += 1

#     def full_name(self):
#         if self.f_name in Member.not_allowed_names:
#             raise ValueError('this name in not allowed')
#         else:
#             return f"{self.f_name} {self.m_name} {self.l_name}"

#     def sayHello(self):
#         if self.gender == 'Male':
#             return f"Hello Mr. {self.f_name}"
#         elif self.gender == 'Female':
#             return f"Hello Miss. {self.f_name}"
#         else:
#             return f"Hello {self.f_name}"

#     def get_all_info(self):
#         return f"{self.sayHello()}, Your full name is: {self.full_name()}"

#     def delete_user(self):
#         Member.user_count -= 1
#         return f"user {self.f_name} is deleted"


# Member.show_user_count()
# member_one = Member('Badre', 'Basem', 'Simon', 'Male')
# member_two = Member('Takmina', 'Aktar', 'Idon', 'Female')
# member_three = Member('Takmina', 'Aktar', 'Idon', 'Female')

# Member.show_user_count()
# print('-' * 20)
# print(member_one.full_name())
# print(Member.full_name(member_three))
# print('-' * 20)
# Member.say_hi()


# -------------------------------------------------
# --OOP-Part-7 => Magic Methods
# ---------------------------------------------
# Everything in Python Is an Object
# __init__ called autometically when instantiating class
# 'self.__class__' the class which a instance class belongs to
# __str__ Gives a humen-readable output of the Object
# __len__ Return the length of the container
#         called when we use the built-in len() function on the object
# -------------------------------------------------------

# class Skills:
#     def __init__(self):
#         self.skills = ['Html', 'Css', 'JS']

#     def __len__(self):
#         return len(self.skills)

#     def __str__(self):
#         return f"My Skills {self.skills}"


# my_skills = Skills()
# print(my_skills)
# my_skills.skills.append('PHP')
# my_skills.skills.append('MySql')
# print(len(my_skills))
# print(my_skills)

# print(my_skills.__class__)


# name ='Simon'
# print(type(name))
# print(name.__class__)
# print(dir(str))
# print(str.upper(name))


# ------------------------------------------------
# --OOP-Part-8 => Inheritance---
# -----------------------------------------

# class Food:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print(f'{self.name} from Base class')

#     def eat(self):
#         print(f'I eat {self.name} from base class')


# class Apple(Food):
#     def __init__(self, name, price, amount):
#         # Food.__init__(self, name, price) # super() method is in place of it
#         super().__init__(name, price)
#         self.amount = amount
#         print(
#             f'{self.name} from child class and price {self.price} and amount {self.amount}')

#     def get_apple(self):
#         print(f'got {self.name} from tree')


# # my_food = Food('pizza', 20)
# my_apple = Apple('Apple', 120, 30)
# my_apple.eat()
# my_apple.get_apple()


# ------------------------------------------------
# --OOP-Part-9 => Multiple Inheritance---
# -----------------------------------------

# class BaseOne:
#     def __init__(self):
#         print('Hello from Base One')

#     def funOne(self):
#         print('One')


# class BaseTwo:
#     def __init__(self):
#         print('Hello from Base Two')

#     def funTwo(self):
#         print('Two')


# class Child(BaseOne, BaseTwo):
#     pass


# my_child = Child()
# print(Child.mro())

# my_child.funOne()
# my_child.funTwo()

# ------------------------------------------------
# --OOP-Part-10 => Polymorephism---
# -----------------------------------------
# a = 12
# b = 12
# print(a + b)

# s1 = 'Hello'
# s2 = 'Simon'
# print(s1 + " " + s2)

# print(len([1, 2, 3, 4]))
# print(len('Hello Python'))
# print(len({'key_one': 1, 'key_two': 2}))

# class A:
#     def do_something(self):
#         raise NotImplementedError('child class must implemente the method')


# class B(A):
#     def do_something(self):
#         print('Hello from B')


# class C(A):
#     def do_something(self):
#         print('Hello from C')


# b = B()
# b.do_something()

# c = C()
# c.do_something()

# ------------------------------------------------
# --OOP-Part-11 => Encapsulation---
# -----------------------------------------
# Encapsulation =>
# ---Restrict Access to the data stored in attributes and methods
# Public => Attributs and methods that can be modified and run from everywhere inside or outside of the class
# Protected =>
# --- Attributs and methods that can be access within the class and sub class/child class
# --- Attributs and methods that prifixed with one underscore _
# Private =>
# --- Attributs and methods that can be access within class or object only
# --- Attributs and methods that can't modified from outside of the class
# --- Attributs and methods that prifixed with two underscore __
# ---------------------------------------------------------------

# class User:
#     def __init__(self, name):
#         self.name = name    # it's Public
#         print(f'Hello {self.name}')

# class User:
#     def __init__(self, name):
#         self._name = name    # it's Protected


# class User:
#     def __init__(self, name):
#         self.__name = name    # it's Private

#     def say_hi(self):
#         return f"Hello {self.__name}"


# user = User('Simon')
# print(user.__name)
# print(user._User__name)
# print(user.say_hi())

# ------------------------------------------------
# --OOP-Part-12 => getter and setter---
# -----------------------------------------

# class User:
#     def __init__(self, name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

#     def set_name(self, new_name):
#         self.__name = new_name

# user = User('simon')
# print(user.get_name())
# user.set_name('Jimon')
# print(user.get_name())

# class Person: 
#     def __init__(self, name, age, email):
#         self.__name = name
#         self.__age = age
#         self.__email = email
    
#     def get_person_info(self):
#         return f'{self.__name.capitalize()}\'s details: \n Name: {self.__name} \n Age: {self.__age} \n Email: {self.__email}'

#     def set_persom_info(self, new_name, new_age, new_email):
#         self.__name = new_name
#         self.__age = new_age
#         self.__email = new_email


# p1 = Person('Simon', 29, 'email@email.com')
# print(p1.get_person_info())
# p1.set_persom_info('jimon', 27, 'test@email.com')
# print(p1.get_person_info())

# ------------------------------------------------
# --OOP-Part-13 => @Property Decorator---
# -----------------------------------------
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def say_hi(self):
#         return f"Hello {self.name}"

#     @property
#     def get_age_in_days(self):
#         return self.age * 365


# user = User('simon', 28)

# # print(user.get_age_in_days())
# print(user.get_age_in_days)


# ------------------------------------------------
# --OOP-Part-14 => ABCs Abstract Base Class---
# --------------------------------------------------------
# class called abstract class when it has one or more abstract methods
# abc module in python provides infrastructure for defining abstract base class
# by adding @abstractmethod decorator on the method
# ABCMeta class is Meta class used for defining abstract base class
# -------------------------------------------------------------

# from abc import ABCMeta, abstractmethod


# class Programming(metaclass=ABCMeta):

#     @abstractmethod
#     def has_oop(self):
#         pass


# class Python(Programming):
#     def has_oop(self):
#         return "Yes"


# class Pascale(Programming):
#     def has_oop(self):
#         return "No"


# lang = Programming()
# print(lang.has_oop())

# lang = Python()
# print(lang.has_oop())

# lang = Pascale()
# print(lang.has_oop())
