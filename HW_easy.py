# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

'''Первый скрипт. Служит для создания папок.'''
import os
quantity = 9
for number in range(quantity):
    dir = "dir_" + str(number+1)
    if dir in os.listdir():
        pass
    else:
        os.mkdir(dir)
print("Папки были созданы.")

'''Второй скрипт. Служит для удаления папок'''
import os
import shutil
quantity = 9
for number in range(quantity):
    dir = "dir_" + str(number+1)
    if dir in os.listdir():
        shutil.rmtree(dir)
    else:
        pass
print("Папки были удалены!")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os
lst = list()
print("Список папок в текущей папке:")
for i in (os.walk(top=os.getcwd())):
    lst.append(i)
for dir in list(lst[0])[1]:
    print(dir)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os
import re
import shutil
file1 = os.path.basename(__file__)
file = (re.search("(.+)(\.[A-Za-zА-Яа-яЁё]+$)", file1))
file2 = file.group(1)+" – copy"+file.group(2)
shutil.copyfile(__file__, file2)