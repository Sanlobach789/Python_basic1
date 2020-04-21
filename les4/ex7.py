def fibo_gen(x):
    result = 1
    for el in list(range(1, x + 1)):
        result *= el
        yield result


var = int(input("Введите число "))

i = 1

for el in fibo_gen(var):
    if i > 15:
        break
    print(el)
    i += 1
