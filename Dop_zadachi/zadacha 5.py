a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
c = a + b
if c % 5 == 0:
    d = c + 1
    print("Крутно 5:", d)
else:
    d = c - 2
    print("Не кратно 5:", d)
