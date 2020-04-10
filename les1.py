some_var1 = 5
some_var2 = 8
print(some_var1, some_var2)
some_user_var1 = input("Введите переменную 1 \n")
some_user_var2 = input("Введите переменную 2 \n")
print(some_user_var1, some_user_var2)

seconds = input("Введите время в секундах \n")
seconds = int(seconds)
sec = seconds % 60
hours = seconds // 3600
minutes = seconds // 60 - hours * 60
result = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(sec))
print(result)


