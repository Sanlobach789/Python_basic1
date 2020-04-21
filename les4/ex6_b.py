from itertools import cycle
from time import sleep

some_list = [12, 23, 45]

for el in cycle(some_list):
    print(el)
    sleep(0.5)
