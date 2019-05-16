#


myString = 'Hi I am ready to learn'
myList = [1, 2, 3, 'asdad', 'gggg[']

# print(myString[::-1])

vari = 104.32442343241241344

# print(f'Variabila are valoarea {vari:1.2f}')

# myDict = {'key1': "value1"}
# print(myDict['key1'])

# with open('D:\\PROJECTS\\Complete-Python-3-Bootcamp\\00-Python Object and Data Structure Basics\\test.txt',
#           'r+') as file:
#     file.write('\nSixth line?')
#     content = file.readlines()
#
# print(content)

# def myfunc(string):
#     for index, letter in enumerate(string):
#         if index % 2:
#             string[index] = string[index].upper()

# def old_macdonald(name):
#     myList = list()
#     for index, a in enumerate(name):
#         if index == 0 or index == 3:
#             myList.append(name)
#         else:
#             myList.append(name.upper())
#     return ''.join(x for x in myList)
#
# print(old_macdonald('macdonald'))

import string


def ispangram(str1, abc=string.ascii_lowercase):
    for letter in str1:
        if letter.lower() in abc:
            abc.replace(letter.lower(), "")
    print(abc)


ispangram("The quick brown fox jumps over the lazy dog")
