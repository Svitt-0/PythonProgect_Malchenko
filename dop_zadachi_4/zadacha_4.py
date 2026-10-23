n = int(input("Введите n: "))
summa = 0
fact = 1
i = 1
while i <= n:
    fact *= i
    summa += fact
    i += 1
print("Сумма факториалов:", summa)