import sys
sys = sys.stdin.readline

n, m = map(int, input().split())
w = []
for i in range(n):
    w.append(int(input()))

w.sort()

# 구하고자 하는 수보다 작은 것들만 활용
start=n-1
while w[start]>m:
    start-=1

ans = 0  # 정답
while m>0:
    if m>=w[start]:
        ans += int(m/w[start])
        m-=(int(m/w[start]))*w[start]
        
    start-=1

print(ans)