# -----------------------------------
# Loop on many iterators with zip()
# -----------------------------------
# zip() returns a zip object contains all objects
# zip() length is the length of lowest object
# -----------------------------------------------------
list1 = [1, 2, 3, 4]
list2 = ['A', 'B', 'C']
tuple1 = ('Man', 'Women', 'Girl', 'boy')
dict1 = {'name': 'simon', 'age': 28, 'country': 'Bangladesh'}


for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):
    print('Item 1 =>', item1)
    print('Item 2 =>', item2)
    print('Item 3 =>', item3)
    print('Item 4 =>', item4, 'value =>', dict1[item4])


# for item in zip(list1, list2):
#     print(item)
