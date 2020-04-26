origin_list = []
with open('/Users/aleksandrlobach/projects/learn_python/Python_basic1/files/task6.txt') as f_obj:
    origin_txt = f_obj.read()
    origin_list = origin_txt.split('\n')

lessons_dict = {}
new_dict = dict()

for itm in origin_list:
    itm_list = itm.split(': ')
    lessons_dict[itm_list[0]] = itm_list[1].split(' ')

for key, value in lessons_dict.items():
    new_dict[key] = sum([int(el.split('(')[0]) for el in value if el.split('(')[0].isdigit()])

print(new_dict)