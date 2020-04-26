from random import randint

numb_list = [randint(1, 100) for el in range(5)]
with open('/Users/aleksandrlobach/projects/learn_python/Python_basic1/files/task5.txt', 'w') as f:
    f.write(' '.join(list(map(lambda x: str(x), numb_list))))
print(numb_list)
with open('/Users/aleksandrlobach/projects/learn_python/Python_basic1/files/task5.txt') as f_2:
    numbers = f_2.read()
    numbers_list = list(map(lambda x: int(x), numbers.split(' ')))
    print(sum(numbers_list))
