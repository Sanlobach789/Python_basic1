def fibo_gen(x):
    result = 1
    for el in list(range(1, x + 1)):
        result *= el
        yield result


var = int(input())

res = [el for el in fibo_gen(var)]

i=0
while i <= len(res) - 1 and i <= 14:
    print(res[i])
    i += 1