n = int(input())
arr = [25, 10, 5, 1]

for i in range(n):
    m = int(input())
    cnt = 0

    for j in range(len(arr)):
        cnt = int(m / arr[j]) # 몫
        m = int(m % arr[j]) # 나머지

        print(cnt, end=' ')

    print("")

# 25 10 5 1