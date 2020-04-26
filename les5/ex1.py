import os

f = open("/Users/aleksandrlobach/projects/learn_python/Python_basic1/files/txtfile.txt", "a")
some_str = ' '
while some_str != '':

    some_str = input("Введите строку: ")
    f.write(some_str + '\n')

f.close()
