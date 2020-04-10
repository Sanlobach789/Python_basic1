some_numb = input("введите число: ")
max_numb = int(some_numb) % 10
some_numb = int(some_numb) // 10
while some_numb > 0:
    if some_numb % 10 > max_numb:
        max_numb = some_numb
    some_numb = some_numb // 10
print(max_numb)