import sys

input = sys.stdin.readline

n = int(input())
dp = [[0]*10 for _ in range(n)]

# 초기화
for i in range(1, 10):
    dp[0][i] = 1

# dp 순환
for i in range(n-1):
    for j in range(10):
        if j==0:
            dp[i+1][j] = dp[i][j+1]
        elif j==9:
            dp[i+1][j] = dp[i][j-1]
        else:
            dp[i+1][j] = dp[i][j-1] + dp[i][j+1]

print(sum(dp[n-1]) % 1000000000)