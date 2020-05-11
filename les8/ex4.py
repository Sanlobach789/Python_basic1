class OfficeEquipment:
    name = 'Название'
    model = 'Модель'
    place = 1
    price = 0
    count = 0

    def __str__(self):
        return '{0} ({1}): Place={2}, Price={3}'.format(self.name, self.model, self.place, self.price)


class Xerox(OfficeEquipment):
    copy_speed = 100

    def __init__(self, copy_speed):
        self.copy_speed = copy_speed


class Printer(OfficeEquipment):
    def __init__(self, print_speed, colors):
        self.print_speed = print_speed
        self.colors = colors


class Scaner(OfficeEquipment):
    def __init__(self, sensor):
        self.sensor = sensor


class Warehouse:
    __warehouse_list = []
    __unit_dict = {}


    def __init__(self, name, places, address):
        self.name = name
        self.places_count = places
        self.address = address

    def reception(self, obj: OfficeEquipment, count):
        if self.places_count - obj.place * count >= 0:
            obj.count += count
            self.__warehouse_list.append(obj)
            self.places_count -= obj.place * count
        else:
            print('на складе нет места')
        for el in self.__warehouse_list:
            print("Принято на склад: " + str(el) + " в количестве: " + str(el.count))

    def transfer(self, office_name: str, equipment_name: str, count):
        unit_name = office_name
        for el in self.__warehouse_list:
            if el.name == equipment_name:
                if el.count >= count:
                    self.places_count += el.place * count
                    index = self.__warehouse_list.index(el)
                    itm = self.__warehouse_list.pop(index)
                    tmp_dict = {unit_name: itm, 'Количество: ': count}
                    self.__unit_dict.update(tmp_dict)

                else:
                    print('нет такого количества оборудования на складе, в наличие: ' + str(el.count))
            else:
                print('оборудования с таким именем нет на этом складе')

    def warehouse_info(self):
        print('Наименование склада: ' + self.name + '\n' + 'Адрес склада: ' + self.address + '\n'
              + 'Количество мест на складе: ' + str(self.places_count))


warehouse = Warehouse('sklad', 30, 'shosse neft')

warehouse.warehouse_info()

scaner = Scaner('laser')
scaner.name = 'scaner'
scaner.model = 'Модель scaner'
scaner.price = 4500

xerox = Xerox('ttt')
xerox.name = 'Xerox'
xerox.model = 'Модель Xerox'
xerox.place = 2
xerox.price = 15900

warehouse.reception(scaner, 1)
warehouse.reception(xerox, 5)

warehouse.warehouse_info()

warehouse.transfer('HR', "Xerox", 3)

warehouse.warehouse_info()



