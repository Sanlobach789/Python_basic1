seconds = input("Введите время в секундах \n")
seconds = int(seconds)
sec = seconds % 60
hours = seconds // 3600
minutes = seconds // 60 - hours * 60
result = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(sec))
print(result)