import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

q = deque(range(1, n+1))

ans = []

# rotate(+1) : 맨 끝 원소가 앞으로 온다
# rotate(-1) : 맨 앞 원소가 뒤로 간다

while q:
    q.rotate(-(k-1))  # EX) 시작점이 1일 때 3 제거, 이후 시작점이 4이고 6 제거
    ans.append(q.popleft())

# 출력
print('<', end='')

for i in range(n):
    if i == n-1:  # 마지막
        print(ans[i], end='')
        break
    print(ans[i], end=', ')

print('>')