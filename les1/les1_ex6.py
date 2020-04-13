a = int(input("Введите значение a "))
b = int(input("Введите значение b "))
i = 1
while a < b:
    a = a * 1.1
    i += 1
print("Спортсмен пробежал " + str(b) + " км" + " на " + str(i) + " день")