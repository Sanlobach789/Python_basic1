def translate(word):
    if word == 'One':
        return 'Один'
    elif word == 'Two':
        return 'Два'
    elif word == 'Three':
        return 'Три'
    elif word == 'Four':
        return 'Четыре'


list_of_dict = []
with open('/Users/aleksandrlobach/projects/learn_python/Python_basic1/files/task4.txt') as some_file:
    value_list = (some_file.read()).split('\n')

for line in value_list:
    line_split = line.split('—')
    list_of_dict.append({'word': line_split[0], 'digit': line_split[1]})

with open('/Users/aleksandrlobach/projects/learn_python/Python_basic1/files/task4_result', 'w') as result_file:
    result_file.write(
        '\n'.join(
            list(
                map(lambda itm: translate(itm.get('word')) + '-' + itm.get('digit'), list_of_dict)
            )
        )
    )
