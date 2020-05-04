class Cell:

    def __init__(self, count):
        self.cell_count = '*' * count

    def __add__(self, other):
        return self.cell_count + other.cell_count

    def __sub__(self, other):
        result = '*' * (len(self.cell_count) - len(other.cell_count))
        if result != '':
            return result
        else:
            return print('Ошибка, отрицательное значение')

    def __mul__(self, other):
        result = '*' * (len(self.cell_count) * len(other.cell_count))
        return result

    def __truediv__(self, other):
        result = '*' * (len(self.cell_count) // len(other.cell_count))
        return result

    def __iter__(self):
        return self.cell_count.__iter__()

    def make_order(self, count):
        pass


test1 = Cell(15)
test2 = Cell(2)
print(test1.__iter__())