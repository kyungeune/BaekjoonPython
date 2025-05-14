import sys
input = sys.stdin.readline
# 0. 변수 초기화 및 입력
n = int(input())
p = list(map(int, input().split()))
ans = 0


# 1. 
p.sort()
for i in range(n):
    ans += (n-i)*p[i]

print(ans)