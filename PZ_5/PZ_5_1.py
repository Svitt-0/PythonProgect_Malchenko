#Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить
# функцией с параметрами. Значения n и m программа должна запрашивать.
def find_sum(n, m):
    total = 0
    while n <= m:
        total = total + n
        n = n+1
    return total
try:
    n = int(input("Введите число n:"))
    m = int(input("Введите число m:"))
    print("Сумма чисел равна:", find_sum(n, m))
except ValueError:
    print("Ошибка. Введите целые числа")