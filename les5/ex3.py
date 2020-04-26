from functools import reduce


def find_avg(array):
    sum_salary = 0
    for itm in array:
        sum_salary += int(itm.get('salary'))
    avg_salary: float = sum_salary / len(array)
    return avg_salary


file_salary = open('/Users/aleksandrlobach/projects/learn_python/Python_basic1/files/task3.txt')
salary_data = (file_salary.read()).split('\n')

result_list = []
for line in salary_data:
    line_split = line.split(' ')
    result_list.append({'name': line_split[0], 'salary': line_split[1]})

salary_filtered = list(filter(lambda x: int(x.get('salary')) < 20000, result_list))

print('Сотрудники, которые имеют ЗП ниже 20к в мес.: %s' % [itm.get('name') for itm in salary_filtered])

print('\nСредняя ЗП сотрудников компании: %.2f' % find_avg(result_list))
print('\nСредняя ЗП сотрудников компании у которых менее 20к ЗП: %.2f' % find_avg(salary_filtered))
