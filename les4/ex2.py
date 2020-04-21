from random import randint


numb_list = [el for el in range(randint(10, 500))]
i = 0
new_list = []
while i < len(numb_list) - 1:
    if numb_list[i] < numb_list[i+1]:
        new_list.append(numb_list[i+1])
    i += 1
print(new_list)