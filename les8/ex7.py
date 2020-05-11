class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return '{0} + {1}i'.format(a, b)

    def __mul__(self, other):
        ac = self.a * other.a
        bd = self.b * other.b
        ad = self.a * other.b
        bc = self.b * other.a

        first_result = ac - bd
        second_result = ad + bc

        return '{0} + {1}i'.format(first_result, second_result)


t = ComplexNumber(3, 0)
r = ComplexNumber(2, 6)

result_add = t + r
result_mul = t * r

print('Результат сложения: {0}'.format(result_add))
print('Результат умножения: {0}'.format(result_mul))