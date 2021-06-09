# ----------------------------------
# --Regular Expressions => Intro
# ------------------------------------
# [1] Sequence of characgters that define a search pattern
# [2] RegEx is not in python it's general concept
# [3] Used in (Cradit card validation, IP Address Validation, Email validation)
# [4] Test RegEx "https://pythex.org/"
# [5] Charater sheet "https://www.debuggex.com/cheatsheet/regex/python"
# --------------------------------------------


# --------------------------
# --part-2 Quantifires
# ----------------------
# * 0 or more
# + 1 or more
# ? 0 or one
# {2} exactly two
# {2, 5} between two and five
# {2,} 2 or more
# (, 5} up to 5
# 'https://regex101.com/'
# ----------------------------------------------------------


# --------------------------
# --part-3 Characters Classes Traing
# ------------------------------------
# [0-9]
# [^0-9]
# [A-Z]
# [^A-Z]
# [2, 5] between two and five
# [a-z]
# [^a-z]
#  \s[A-Z]{2}\s[0-9]{3}\s\w{,5} =>  OS 123 simon
# ----------------------------------------------------------


# --------------------------
# --part-4 Assertions
# ------------------------------------
# ^ START OF STRING
# $ END OF STRING

# match mobile number
# ^\d{3}\s\d{4}-?\s?\d{4}$ => 012 2264-8162

# macth email
# [A-z0-9\.]+@[A-z0-9]+\.[A-z]+
# ^[A-z0-9\.]+@[A-z0-9]+\.(com|net|io|org|info)$
# ----------------------------------------------------------


# --------------------------
# --part-5 Logical or and Escaping
# ------------------------------------
# | or
# \ escape special characters
# () separate group
# (\d-|\d\)|\d>)\s(\w+) => 1- html, 2) css, 3 > js
# (\d{3})\s(\d{4})\s(\d{4}|\(\d{4}\))  => 012 2264 8162 or 012 2264 (8162)
# ^(https?://)(www\.)?(\w+)\.(io|info|org|com)$ =>  http://www.simon.io
#                                                   http: // simon.org
#                                                   https: // simonkabir.info
# ----------------------------------------------------------


# --------------------------
# --part-6 Re Module search and findAll
# ------------------------------------
# search() => seach a string for a macth and return the first match only
# findall() => return a list of all matches and empty list if no match
# ----------------------------------------------------------------------
# email pattern => [A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)
# ----------------------------------------------------------

# import re

# my_search = re.search('[A-Z]', 'simonKabir')
# print(my_search)
# print(dir(my_search))
# print(my_search.span())
# print(my_search.string)
# print(my_search.group())

# is_email = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", 'simon@email.net')

# if is_email:
#     print('it\'s a valid email')
#     print(is_email.span())
#     print(is_email.string)
#     print(is_email.group())
# else:
#     print('it\'s not a valid email')

# email_input = input('enter your email: ')
# empty_list = []

# email = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net", email_input)

# if email != []:
#     empty_list.append(email)
#     print('email added')
# else:
#     print('invalid email')

# for item in empty_list:
#     print(item)


# --------------------------
# --part-7 Re Module split and sub
# ------------------------------------
# split(pattern, string, maxSplit) => return a list of element splited on every match
# sub(pattern, replace, string, replaceCount) => replace matches with what you want
# ----------------------------------------------------------------------

# import re

# string = 'I Love Python Language'

# spl = re.split(r"\s", string, 2)
# print(spl)

# string = 'I-Love-Python_ as_a_programming_Language'
# spl = re.split(r"-|_", string)
# # print(spl)

# for counter, word in enumerate(spl, 1):
#     if len(word) == 1:
#         continue
#     print(f"word number with value: {counter} => {word}")


# a = 'I Love Python'
# s = re.sub(r'\s', '_', a)
# s = re.sub(r'\s', '_', a, 1)
# print(s)

# --------------------------
# --part-8 Group traning and flags
# ---------------------------------
# import re

# my_web = "https://www.simon.io:4040/info.php?article=156?name=how-to-do"
# s = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)",
#               my_web, re.DOTALL)

# print(s.group())
# print(s.groups())

# for group in s.groups():
#     print(group)

# print(f"Protocol: {s.group(1)}")
# print(f"Sun Domain: {s.group(2)}")
# print(f"Domain name: {s.group(3)}")
# print(f"Top Level Domain: {s.group(4)}")
# print(f"Port: {s.group(5)}")
# print(f"Query String: {s.group(6)}")
