#Дано вещественное число A и целое число N (>0). Используя один цикл, найти значение выражения 1 - A + A² - A³ + ... +(-1)ᴺ Aᴺ. Условный оператор не использовать.
while True:
    try:
        A = float(input("Введите вещественное число A: "))
        N = int(input("Введите целое число N (>0): "))
        break
    except ValueError:
        print("Ошибка! Вы ввели не число. Попробуйте снова.")
total = 1
current_power = 1
sign = -1
i = 1
while i <= N:
    current_power *= A
    total += sign * current_power
    sign *= -1
    i += 1
print("Значение выражения:", total)