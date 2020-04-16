def my_func(x, y, z):
    values = [x, y, z]
    max_a = max(values)
    values.remove(max_a)
    max_b = max(values)
    return print(max_a + max_b)


a = int(input("Введите значение a "))
b = int(input("Введите значение b "))
c = int(input("Введите значение c "))

my_func(a, b, c)
