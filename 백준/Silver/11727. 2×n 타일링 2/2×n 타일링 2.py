import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*1001

dp[1] = 1
dp[2] = 3
# dp[3] = dp[1]*2 + dp[2]

for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]*2
    # dp[i-1] = 111
    # dp[i-2] = 1= 1ㅁ

print(dp[n]%10007)