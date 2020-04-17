result = 0
i = 0
while i != 1:
    usr_numbers = input("Введите числа через пробел (чтобы остановить работу программы наберите любую букву): ")
    numb_list = usr_numbers.split(' ')
    for itm in numb_list:
        try:
            result += int(itm)
        except ValueError:
            i = 1
            print("Программа завершена, результат:")
    print(result)