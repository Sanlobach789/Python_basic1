def usr_data(f_name, l_name, year, city, email, phone):
    return print("Имя: " + f_name + "; Фамилия: " + l_name + "; Год рождения: " + year +
                 "; Город проживания: " + city + "; Email: " + email + "; Телефон: " + phone)


usr_f_name = input("Введите имя ")
usr_l_name = input("Введите фамилию ")
usr_year = input("Введите год рождения ")
usr_city = input("Введите город проживания ")
usr_email = input("Введите email ")
usr_phone = input("Введите номер телефона ")
usr_data(f_name=usr_f_name, l_name=usr_l_name, year=usr_year, city=usr_city, email=usr_email, phone=usr_phone)
