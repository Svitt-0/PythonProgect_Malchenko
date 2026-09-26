#Дано трехзначное число. Найдите сумму и произведение его цифр
try:
    number = input("Введите трехзначное число: ")
    if len(number) != 3:
        int("ошибка")

    a = int(number[0])
    b = int(number[1])
    c = int(number[2])

    print("Сумма:", a + b + c)
    print("Произведение:", a * b * c)

except ValueError:
    print("Ошибка. Нужно ввести ровно 3 цифры.")

