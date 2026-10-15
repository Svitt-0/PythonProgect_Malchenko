#Даны три целых числа: А,В, С. Проверить истинность высказывания: "Ровно два из чисел А, В, С являются положительными".
while True:
    try:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))
        break
    except ValueError:
        print("Нужно ввести цифрами")

if a > 0 and b > 0 and c <= 0:
    print("Истина")
elif a > 0 and c > 0 and b <= 0:
    print("Истина")
elif b > 0 and c > 0 and a <= 0:
    print("Истина")
else:
    print("Ложь")
