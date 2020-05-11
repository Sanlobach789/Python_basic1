from time import sleep
from itertools import cycle
import datetime


class TrafficLight:
    def __init__(self, go, wait, stop):
        self.__color = [go, wait, stop]

    def running(self):
        t = str(datetime.datetime.time(datetime.datetime.now()))
        correct_order = ['red', 'yellow', 'green']
        new_list = [i for i in self.__color if i == correct_order[self.__color.index(i)]]
        if len(new_list) < 3:
            print('Wrong order')
        else:
            self.__color.append('yellow')
            for i in cycle(self.__color):
                if i == 'yellow':
                    print(f'\033[33m{i}')
                    sleep(2)
                elif i == 'red':
                    print(f'\033[31m{i}')
                    sleep(7)
                else:
                    print(f'\033[32m{i}')
                    sleep(7)
                if 0 <= int(t[:2]) <= 5:
                    break


a = TrafficLight('red', 'yellow', 'green')
a.running()