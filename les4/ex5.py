from functools import reduce

numb_list = [itm for itm in range(100, 1001, 2)]
result = reduce(lambda x,y: x+y, numb_list)

print(result)