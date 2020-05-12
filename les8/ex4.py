import functools
import copy

class OfficeEquipment:
    name = 'Название'
    place = 1
    price = 0

    def __str__(self):
        return '{0}: Place={1}, Price={2}'.format(self.name, self.place, self.price)


class Xerox(OfficeEquipment):
    copy_speed = 100

    def __init__(self, name, place, price, copy_speed):
        self.name = name
        self.place = place
        self.price = price
        self.copy_speed = copy_speed


class Printer(OfficeEquipment):
    print_speed = 50
    colors = 2

    def __init__(self, name, place, price, print_speed, colors):
        self.name = name
        self.place = place
        self.price = price
        self.print_speed = print_speed
        self.colors = colors


class Scaner(OfficeEquipment):
    sensor = 'laser'

    def __init__(self, name, place, price, sensor):
        self.name = name
        self.place = place
        self.price = price
        self.sensor = sensor


class Warehouse:
    __warehouse_list = []
    __unit_dict = {}

    name = 'Название'
    places_count = 50

    def __init__(self, name, places_count, address):
        self.name = name
        self.places_count = places_count
        self.address = address

    def __total_free(self) -> int:
        if len(self.__warehouse_list) == 0:
            current_used = 0
        else:
            equip_space = list(map(lambda x: x.get('count') * x.get('equipment').place, self.__warehouse_list))
            current_used = functools.reduce(lambda a, b: a + b, equip_space)
        return self.places_count - current_used

    def __is_free(self, obj, count) -> bool:
        return self.__total_free() - (obj.place * count) >= 0

    def __get_index_by_name(self, name: str) -> int:
        index = -1
        for el in self.__warehouse_list:
            if el.get('equipment').name == name:
                index = self.__warehouse_list.index(el)
                break
        return index

    def reception(self, obj: OfficeEquipment, count):
        if self.__is_free(obj, count):
            index = self.__get_index_by_name(obj.name)
            if index < 0:
                self.__warehouse_list.append({'equipment': obj, 'count': count})
            else:
                self.__warehouse_list[index]['count'] += count
            print("Принято на склад: {0} в кол-ве {1} шт.".format(str(obj), count))
        else:
            print('на складе нет места')

    def transfer(self, office_name: str, equipment_name: str, count: int = 1):
        if count < 1:
            print('Нельзя перенести менее одной штуки')
            return

        unit_name = office_name
        index = self.__get_index_by_name(equipment_name)

        copy_warehouse = copy.deepcopy(self.__warehouse_list)
        if index < 0:
            print('оборудования с таким именем нет на этом складе')
            return
        if copy_warehouse[index].get('count') < count:
            print('оборудования с запрашиваемым количеством нет на этом складе')
            return
        elif copy_warehouse[index].get('count') == count:
            item = copy_warehouse.pop(index)
        else:
            item = copy_warehouse[index]
            copy_warehouse[index]['count'] = copy_warehouse[index].get('count') - count
            self.__warehouse_list = copy_warehouse

        dict_element = self.__unit_dict.get(unit_name)
        if dict_element is None:
            dict_element = {unit_name: [item]}
        else:
            equip_index = -1
            for el in dict_element:
                if el.get('equipment').name == equipment_name:
                    equip_index = dict_element.index(el)
                    break
            if equip_index < 0:
                dict_element.append(item)
            else:
                dict_element[equip_index]['count'] += count
        self.__unit_dict.update(dict_element)

    def warehouse_info(self):
        tmp = '\nНаименование склада: {0}\nАдрес склада: {1}\nКоличество мест на складе: {2} из {3}\n'
        print(tmp.format(self.name, self.address, str(self.__total_free()), self.places_count))


warehouse = Warehouse('sklad', 24, 'shosse neft')

warehouse.warehouse_info()

scaner = Scaner('scaner', 2, 4500, 'laser')
xerox = Xerox('Xerox', 4, 15900, 150)

warehouse.reception(scaner, 2)
warehouse.warehouse_info()
warehouse.reception(xerox, 5)

warehouse.warehouse_info()
warehouse.transfer('HR', "Xerox", 2)
warehouse.warehouse_info()
warehouse.transfer('HR', "Xerox", 1)
warehouse.warehouse_info()