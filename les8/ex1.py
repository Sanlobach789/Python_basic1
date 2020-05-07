class Date:
    day = 1
    month = 1
    year = 1
    @classmethod
    def parse(cls, param):
        date = param.split('-')
        int_date = []
        try:
            for itm in date:
                int_date.append(int(itm))
        except ValueError:
            print('Пожалуйста, введите дату в правильном формате (Например: 01-01-2020): ')
        cls.day = int_date[0]
        cls.month = int_date[1]
        cls.year = int_date[2]

    @staticmethod
    def Validation(obj):
        if 0 > obj.day or obj.day > 30:
            print('Введена некорректная дата')
        if 0 > obj.month or obj.month > 12:
            print('Введена некорректная дата')
        if 0 > obj.year:
            print('Введена некорректная дата')


usr_date = input('Введите дату в формате "день-месяц-год": ')
t = Date()
t.parse(usr_date)
Date.Validation(t)
print(t.day)
print(t.month)
print(t.year)

