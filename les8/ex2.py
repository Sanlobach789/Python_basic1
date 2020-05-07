class WrongDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


var_1 = int(input('Введите первую переменную '))
var_2 = int(input('Введите вторую переменную '))

try:
    if var_2 == 0:
        raise WrongDiv("Делить на ноль нельзя!")
except WrongDiv as err:
    print(err)
else:
    print(var_1 / var_2)
