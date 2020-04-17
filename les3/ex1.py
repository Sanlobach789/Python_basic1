def div(a, b):
    try:
        return print(a/b)
    except ZeroDivisionError:
        print("Лучше не делить на 0...")


var1 = int(input("Введите число a: "))
var2 = int(input("Введите число b: "))
div(var1, var2)
