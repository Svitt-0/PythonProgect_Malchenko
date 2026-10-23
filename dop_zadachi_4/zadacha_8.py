a = int(input("Введите A: "))
b = int(input("Введите B: "))
summa = 0
i = a
while i <= b:
    summa += i
    i += 1

print("Сумма чисел от A до B:", summa)