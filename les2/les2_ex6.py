from typing import List

good_id = 0
total_list = {}
while good_id <= 2:
    item = input("Введите характеристики товара через запятую 'название цена количество единица измерения': ")
    good_char = list(item.split(","))
    if len(good_char) > 4:
        print("Вы ввели больше характеристик.")
    elif len(good_char) < 4:
        print("Вы ввели не все характеристики")
    elif len(good_char) == 4:
        good_id += 1
        goods = {"": good_id,
                 "Название ": str(good_char[0]),
                 "Цена ": str(good_char[1]),
                 "Количество ": str(good_char[2]),
                 "ед.": str(good_char[3])}
        print(goods)
        total_list = dict(list(total_list.items()) + list(goods.items()))
print(total_list)