summa = 0
kolvo = 0
i = 1
while i <= 4:
    num = int(input("Введите число: "))
    if num < 0:
        summa += num
        kolvo += 1
    i += 1
print("Сумма отрицательных:", summa)
print("Количество отрицательных:", kolvo)