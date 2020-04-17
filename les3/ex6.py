def int_func(text: str):
    return print(text.title())


usr_words = input("Введите слова через пробел ")
usr_words.lower()
int_func(usr_words)