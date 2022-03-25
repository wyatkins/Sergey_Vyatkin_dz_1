mylist = []
# получаем список нечетных в кубе
for i in range(1, 1001):
    if (i % 2 != 0):
        mylist.append(i ** 3)
print(mylist)

# отбираем из списка то, что делится на 7 без остатка
# for i in mylist:
#    if (i % 7 == 0):
#        print(i)

sum_1 = 0
for i in mylist:
    sum = 0
    num_saved = i
    while (i != 0):
        sum = sum + i % 10
        i = i // 10
        if sum % 7 == 0:
            sum_1 = sum_1 + num_saved
print(sum_1)

# добавление к каждому элементу списка 17
for i in range(len(mylist)):
    mylist[i] += 17
print(mylist)

# и новая сумма из списка
for i in mylist:
    sum = 0
    num_saved = i
    while (i != 0):
        sum = sum + i % 10
        i = i // 10
        if sum % 7 == 0:
            sum_1 = sum_1 + num_saved
print(sum_1)