from time import sleep


class TrafficLight:
    __color = ['RED', 'Yellow', 'GREEN']

    def running(self):
        color = TrafficLight.__color
        self.__color = color[0]
        print(self.__color)
        sleep(7)
        self.__color = color[1]
        print(self.__color)
        sleep(2)
        self.__color = color[2]
        print(self.__color)
        sleep(5)


t = TrafficLight()
t.running()
