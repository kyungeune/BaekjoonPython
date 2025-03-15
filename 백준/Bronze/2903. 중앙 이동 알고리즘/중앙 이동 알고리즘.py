n = int(input())

k = 2

for i in range(n):
    k += (k - 1)

print(k * k)