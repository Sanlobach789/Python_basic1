gain = input("Введите значение прибыли: ")
costs = input("Введите значение издержек: ")
if int(gain) > int(costs):
    efficiency = int(gain) / int(costs)

    print("Эффективность фирмы составила " + str("{:.3f}".format(efficiency)))
    hr = input("Введите количество сотрудников в фирме ")
    h_eff = efficiency / int(hr)
    print("Прибыль фирмы в расчете на сотрудника " + str("{:.3f}".format(h_eff)))
else:
    print("Издержки превышают прибыль")