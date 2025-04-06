import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
which = list(map(int, input().split()))  # 큐냐 스택이냐
first = list(map(int, input().split()))  # 원소 초기값

m = int(input())
plus = list(map(int, input().split()))  # 넣어야 하는 원소들

q = deque()
ans = []

for i in range(n-1, -1, -1):  # 큐 초기화
    if which[i] == 0:
        q.append(first[i])

for i in plus:
    q.append(i)
    print(q.popleft(), end=' ')

# for j in plus:
#     q.append(j)
#     for i in range(n):
#         if which[i] == 0:
#             q.append(q[i])
#     ans.append(q.pop())

# print(*ans)