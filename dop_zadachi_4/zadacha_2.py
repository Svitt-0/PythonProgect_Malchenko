a = int(input("Введите число:"))
b = int(input("Введите число:"))
c = int(input("Введите число:"))
d = int(input("Введите число:"))
kolvo = 0
if a % 2 == 0:
    kolvo += 1
if b % 2 == 0:
    kolvo += 1
if c % 2 == 0:
    kolvo += 1
if d % 2 == 0:
    kolvo += 1
print(kolvo)