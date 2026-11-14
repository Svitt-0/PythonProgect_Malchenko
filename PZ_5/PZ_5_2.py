#Описать функцию Power1(A, B) вещественного типа, находящую величину AB по
# формуле AB = exp(B*ln(A)) (параметры A и B — вещественные). В случае нулевого
# или отрицательного параметра A функция возвращает 0. С помощью этой функции
# найти степени AP, BP, CP, если даны числа P, A, B, C.
import math
def Power1(A, B):
    if A <= 0:
        return 0
    else:
        result = math.exp(B * math.log(A))
        return result
try:
    print("Введите числа:")
    P = float(input("Введите P:"))
    A = float(input("Введите A:"))
    B = float(input("Введите B:"))
    C = float(input("Введите C:"))
    print("A в степени P равно:", Power1(A, P))
    print("B в степени P равно:", Power1(B, P))
    print("C в степени P равно:", Power1(C, P))
except ValueError:
    print("Ошибка. Нужно вводить только числа")

