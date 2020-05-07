class NumbValid(Exception):
    def __init__(self):
        self.txt = 'Это не число'
        print(self.txt)


result_list = []
usr_str = ''
stop_word = 'stop'
try:
    while usr_str != stop_word:
        usr_str = input('Введите число ')
        if usr_str.isdigit():
            result_list.append(usr_str)
        else:
            print('Это не число')
except NumbValid:
    print()
finally:
    print(result_list)
