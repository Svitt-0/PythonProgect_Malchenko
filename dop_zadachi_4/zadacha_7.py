a = int(input("Введите A: "))
b = int(input("Введите B: "))
count = 0
i = b
while i >= a:
    print(i, end=" ")
    count += 1
    i -= 1
print("\nКоличество чисел:", count)