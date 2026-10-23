count = 0
i = 1
a_i = 3 * i - 2
while a_i < 30:
    if 10 < a_i < 30:
        count += 1
        print("Подходит элемент:", a_i)
    i += 1
    a_i = 3 * i - 2
print("Количество подходящих элементов:", count)