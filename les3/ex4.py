def my_func(x,y):
    result = 1
    i = -1
    while i >= y:
        result = result * x
        i -= 1
    return print("%.3f" % (1 / result))


usr_x = float(input("Введите действительное число "))
usr_y = int(input("Введите отрицательное число "))
my_func(usr_x, usr_y)