from abc import ABC, abstractmethod


class Wear(ABC):

    @property
    @abstractmethod
    def consumption(self) -> float:
        pass

    @property
    @abstractmethod
    def params(self) -> float:
        pass


class Suit(Wear):

    def __init__(self, name, height):
        self.__height = height
        self.name = name

    @property
    def consumption(self) -> float:
        return 2 * self.__height + 0.3

    @property
    def params(self) -> float:
        return self.__height


class Coat(Wear):

    def __init__(self, name, size):
        self.__size = size
        self.name = name

    @property
    def consumption(self) -> float:
        return self.__size / 6.5 + 0.5

    @property
    def params(self) -> float:
        return self.__size


s = Suit('jacket', 29)
print(s.consumption)
c = Coat('coat1', 30)
print(c.consumption)
