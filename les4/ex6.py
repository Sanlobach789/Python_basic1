from itertools import count, cycle
from time import sleep

i = int(input("Введите число для начала "))
for el in count(i):
    print(el)
    sleep(1)
