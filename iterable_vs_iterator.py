# Iterable
# [1] Object contains data that can be iterated upon
# [2] Example (String, List, Set, Tuple, Dictionary)

# Iterator
# Object used to Iterate over iterable using next(), return 1 element at a time
# You can generate iterator from iterable when using iter() Method
# For loop already call the iter() method on the iterable behind the scene
# Gives 'StopIteration' if there is no next element


# numbers = [1, 2, 3, 4, 5, 6]
# for number in numbers:
#     print(number, end=" ")


name = 'Simon'
# myIterator = iter(name)
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))

# for letter in iter(name):
#     print(letter)
# for letter in iter('Simon Kabir'):
#     print(letter)