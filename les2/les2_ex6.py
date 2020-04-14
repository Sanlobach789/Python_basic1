i = 0
goods_list = []
names = []
prices = []
counts = []
units = []
while i <= 2:
    item_id = input("номер товара: ")
    item_id = int(item_id)
    item_name = input("Введите название товара: ")
    item_price = input("Введите цену товара: ")
    item_price = int(item_price)
    item_count = input("Введите количество товара: ")
    item_count = int(item_count)
    item_unit = input("Введите единицу измерения: ")
    good_info = {"Название ": item_name,
                 "цена ": item_price,
                 "количество ": item_count,
                 "Единица измерения ": item_unit}
    good = [(item_id, good_info)]
    goods_list.extend(good)
    names.append(item_name)
    prices.append(item_price)
    counts.append(item_count)
    if item_unit not in units:
        units.append(item_unit)
    i += 1
goods_analytics = {"Название: ": names,
                   "цена: ": prices,
                   "количество: ": counts,
                   "ед: ": units}
print(goods_analytics)