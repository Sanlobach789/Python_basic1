text = input("Введите фразу: ")
text_mas = list(text.split())
i = 0
while i <= len(text_mas) - 1:
    print("\n" + str(i + 1) + ": " + str(text_mas[i]))
    i += 1
