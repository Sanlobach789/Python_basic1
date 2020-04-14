my_list = [7, 5, 3, 3, 2]
new_elem = input("Введите новый элемент рейтинга ")
new_elem = int(new_elem)

if new_elem in my_list:

    my_list.reverse()

    i = my_list.index(new_elem)
    my_list.insert(i + 1, new_elem)

    my_list.reverse()

elif new_elem > max(my_list):
    my_list.insert(0, new_elem)
elif new_elem < min(my_list):
    my_list.append(new_elem)

print(my_list)