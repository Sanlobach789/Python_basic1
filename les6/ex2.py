class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def calc(self):
        print(f"Масса асфальта - {self._lenght * self._width * 25 * 5 / 1000} тонн")


def main():
    while True:
        try:
            road_1 = Road(int(input("Enter width of road in m: ")), int(input("Enter lenght of road in m: ")))
            road_1.calc()
            break
        except ValueError:
            print("Only integer!")