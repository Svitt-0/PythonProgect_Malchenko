#Дано трехзначное число. Найдите сумму и произведение его цифр
while True:
    try:
        number = int(input("Введите трехзначное число: "))
        break
    except ValueError:
        print("Нужно ввести цифрами")
a = number // 100
b = number // 10 % 10
c = number % 10
print("Сумма:", a + b + c)
print("Произведение:", a *  b * c)