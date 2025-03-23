import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

m = [[0] * 3 for _ in range(n)]  # money
m[0][0] = arr[0][0]  # 빨강
m[0][1] = arr[0][1]  # 초록
m[0][2] = arr[0][2]  # 파랑

# 두 번째 집부터 채워나가기
for i in range(1, n):
    m[i][0] = min(m[i-1][1], m[i-1][2]) + arr[i][0]
    m[i][1] = min(m[i-1][0], m[i-1][2]) + arr[i][1]
    m[i][2] = min(m[i-1][0], m[i-1][1]) + arr[i][2]

print(min(m[n-1]))