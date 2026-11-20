#Дан список A размера N. Вывести его элементы в следующем порядке: A1, A2, AN,
# AN-1 , A3 , A4 , AN-2, AN-3, ... .
import random
N = int(input("Введите размер списка N: "))
A = [random.randint(1,99) for _ in range(N)]
print("Исходный список:", A)
print("Ответ:")
left = 0
right = N - 1
while left <= right:
    print(A[left], end= '')
    left += 1
    if left <= right:
        print(A[left], end= '')
        left += 1
    if left <= right:
        print(A[left], end='')
        right -= 1
    if left <= right:
        print(A[left], end='')
        right -= 1

