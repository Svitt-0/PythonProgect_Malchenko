kolvo = 0
i = 1
while i <= 4:
    num = int(input("Введите число: "))
    if num % 2 == 0:
        kolvo += 1
    i += 1
print("Количество четных чисел:", kolvo)