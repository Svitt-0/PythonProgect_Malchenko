n = int(input("Введите количество чисел N: "))
total = 0
i = 1
while i <= n:
    num = float(input("Введите число: "))
    total += num
    i += 1
arif = total / n
print("Среднее арифметическое:", arif)