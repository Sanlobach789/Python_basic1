class Cell:

    def __init__(self, count):
        self.cell_count = count

    def __add__(self, other):
        return '*' * (self.cell_count + other.cell_count)

    def __sub__(self, other):
        result = '*' * (self.cell_count - other.cell_count)
        if result != '':
            return result
        else:
            return print('Ошибка, отрицательное значение')

    def __mul__(self, other):
        result = '*' * (self.cell_count * other.cell_count)
        return result

    def __truediv__(self, other):
        result = '*' * (self.cell_count // other.cell_count)
        return result

    def make_order(self, count):
        i = 0
        counter = 0
        result = ''
        while i < self.cell_count:
            if counter < count:
                result += '*'
                counter += 1
                i += 1
            else:
                result += '\n'
                counter = 0
        print(result)


test1 = Cell(7)
test2 = Cell(2)
print(test1 + test2)
print(test1 - test2)
print(test1 * test2)
print(test1 / test2)
test1.make_order(3)