#Дан список A размера N и целое число K (1 < K < 4, K < N ). Осуществить
# циклический сдвиг элементов списка вправо на K позиций (при этом A 1 перейдет в
# AK+1, A2 — в AK+2, ..., AN — в A K ). Допускается использовать вспомогательный
# список из 4 элементов.
import random
N = int(input("Введите размер списка:"))
A = [random.randint(1, 99) for _ in range(N)]
K = random.randint(2, 3)
print("Исходный список:", A)
print("Сдвиг вправо на", K, "позиций")
for step in range(K):
    last_element = A[N - 1]
    for i in range(N - 1, 0, -1):
        A[i] = A[i - 1]
    A[0] = last_element
print("Результат:", A)