n = int(input())
arr = []

for i in range(n):
    imsi = int(input())
    arr.append(imsi)

arr.sort()

for i in arr:
    print(i)