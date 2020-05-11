class NumbValid(Exception):
    def __init__(self):
        self.txt = 'Это не число'


result_list = []
usr_str = ''
stop_word = 'stop'
while usr_str != stop_word:
    try:
        usr_str = input('Введите число: ')
        if usr_str.isdigit():
            result_list.append(usr_str)
        else:
            raise NumbValid()
    except NumbValid as e:
        print(e.txt)
print(result_list)
