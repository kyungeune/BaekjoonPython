import sys
input = sys.stdin.readline

n = int(input())
sum = [list(map(int, input().split())) for i in range(n)]

for i in range(n-2, -1, -1):  # 맨 마지막 줄 바로 위부터
    for j in range(i+1):  # i의 개수만큼 (정삼각형)
        sum[i][j] += max(sum[i+1][j], sum[i+1][j+1])

print(sum[0][0])