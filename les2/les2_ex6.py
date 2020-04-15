i = 0
goods_list = []
goods_analytics = {"Название": list(),
                   "Цена": list(),
                   "Количество": list(),
                   "Ед": list()}
count = int(input("Кол-во добавляемого товара: "))
while i < count:
    item_id = int(input("номер товара: "))
    item_name = input("Введите название товара: ")
    item_price = int(input("Введите цену товара: "))
    item_count = int(input("Введите количество товара: "))
    item_unit = input("Введите единицу измерения: ")
    good_info = {"Название": item_name,
                 "Цена": item_price,
                 "Количество": item_count,
                 "Ед": item_unit}
    good = [(item_id, good_info)]
    goods_list.extend(good)
    i += 1

for item in goods_list:
    goods_analytics["Название"].append(item[1].get('Название'))
    goods_analytics["Цена"].append(item[1].get('Цена'))
    goods_analytics["Количество"].append(item[1].get('Количество'))
    goods_analytics["Ед"].append(item[1].get('Ед'))

print(goods_analytics)
