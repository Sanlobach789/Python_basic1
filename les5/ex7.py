import json


def read_info():
    with open('/Users/aleksandrlobach/projects/learn_python/Python_basic1/files/task7.txt') as f_obj:
        for line in f_obj:
            el_array = line.split(' ')
            yield {
                'title': el_array[0],
                'type': el_array[1],
                'earn': int(el_array[2]),
                'cost': int(el_array[3])
            }


profits = [dict()]
for itm in read_info():
    profit = itm['earn'] - itm['cost']
    profits[0].update({itm.get('title'): profit})

super_firms = [v for k, v in profits[0].items() if v >= 0]
avg = sum(super_firms) / len(super_firms)
profits.append({'average_profit': avg})

with open('/Users/aleksandrlobach/projects/learn_python/Python_basic1/files/task7.json', 'w') as f_obj:
    json.dump(profits, f_obj)
print(profits)
