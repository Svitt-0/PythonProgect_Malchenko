a = int(input("Введите число:"))
b = int(input("Введите число:"))
c = int(input("Введите число:"))
d = int(input("Введите число:"))
summa = 0
proizved = 0
if a < 0:
    summa += 1
    proizved += a
if b < 0:
    summa += 1
    proizved += b
if c < 0:
    summa += 1
    proizved += c
if d < 0:
    summa += 1
    proizved += d
print(summa, proizved)