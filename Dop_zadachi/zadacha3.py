a = int(input("Введите двухзначное число:"))
dec = a // 10
edin = a % 10
summa = dec + edin
if summa % 2 == 0:
    c = a + 2
    print("Четное число", c)
else:
    c = a - 2
    print("Нечетное число", c)