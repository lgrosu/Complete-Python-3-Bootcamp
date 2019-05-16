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

import os
some = ''
i = 0

while True:
    os.system('cls')
    print('1 | X | X | X |')
    print('---------------')
    print('2 | X | 0 | O |')
    print('---------------')
    print('3 | 0 | X | O |')
    print('---------------')
    print('    A   B   C   ')

    print(some)
    some = input(f'Player {i % 2 + 1} >>')
    i += 1
    if some == 'q':
        break

