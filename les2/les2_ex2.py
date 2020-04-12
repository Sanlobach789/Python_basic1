usr_list = list(input())
print(usr_list)
print(len(usr_list))
i = 0

if (len(usr_list)-1) % 2 == 0:
    while i < len(usr_list) - 1:
        a = usr_list[i]
        b = usr_list[i + 1]
        usr_list[i] = b
        usr_list[i + 1] = a
        i += 2
    print(usr_list)

else:
    while i < len(usr_list) - 2:
        a = usr_list[i]
        b = usr_list[i + 1]
        usr_list[i] = b
        usr_list[i + 1] = a
        i += 2
    print(usr_list)