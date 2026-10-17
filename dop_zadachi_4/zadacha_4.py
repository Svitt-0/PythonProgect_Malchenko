a = int(input("Введите число"))
S = 0
fact = 1
i = 1
while i <= a:
    factorial = fact * i
    S = S + factorial
    i = i + 1
print(S)