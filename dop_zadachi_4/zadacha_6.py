n = int(input("Введите количество чисел N: "))
zero = 0
i = 1
while i <= n:
    num = int(input("Введите число: "))
    if num == 0:
        zero += 1
    i += 1
print("Количество нулей:", zero)