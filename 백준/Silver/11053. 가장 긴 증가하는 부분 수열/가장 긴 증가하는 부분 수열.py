import sys
input = sys.stdin.readline

n = int(input())
l = []

l = list(map(int, input().split()))

# 시간복잡도
# 백준: 1초에 약 1억(10^8)~2억(2*10^8)번 정도의 연산
# 여기서 n<=1000이기에
# O(n^2) -> 약 1000 * 1000 = 1000000번(백만번) 연산

dp = [1]*n

for i in range(1, n):   
    for j in range(i):
        if l[j]<l[i]:
            dp[i] = max(dp[i], dp[j]+1)
    
print(max(dp))