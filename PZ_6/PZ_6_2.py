#Дан целочисленный список размера N, содержащий ровно два одинаковых элемента.
# Найти номера одинаковых элементов и вывести эти номера в порядке возрастания.
import random
N = int(input("Введите размер списка N:"))
A = random.sample(range(1, 100), N)
index1 = random.randint(0, N - 1)
index2 = random.randint(0, N - 1)
while index1 == index2:
    index2 = random.randint(0, N -1)
A[index2] = A[index1]
print("Список:", A)
for i in range(N):
    for j in range(i + 1, N):
        if A[i] == A[j]:
            print("Номера одинаковых элементов:", i + 1, j + 1)