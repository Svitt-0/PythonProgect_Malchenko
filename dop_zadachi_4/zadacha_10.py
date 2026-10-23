n = int(input("Введите N (N >= 3): "))
a = 1
b = 1
count_even = 0
i = 1
while i <= n:
    print(a, end=" ")
    if a % 2 == 0:
        count_even += 1
    c = a + b
    a = b
    b = c
    i += 1
print("\nКоличество четных чисел:", count_even)