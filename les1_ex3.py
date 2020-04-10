input_numb = input("Введите число: ")
i = 1
result_sum = 0
while i <= 3:
    j = 1
    result_str = ""
    while j <= i:
        result_str += input_numb
        j += 1
    print(result_str)
    i += 1
    result_sum += int(result_str)
print(result_sum)