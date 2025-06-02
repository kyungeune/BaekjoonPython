import sys

n = int(input())
order = list(map(int, input().split()))

stack = []
cur = 1  # 간식을 받아야 할 현재 순서

for i in order:
    while stack and stack[-1]==cur:
        stack.pop()  # 스택에서 꺼낼 수 있는 값은 다 꺼내자
        cur+=1

    if i == cur:
        cur += 1
    else:
        stack.append(i)

# 남은 스택 처리
while stack and stack[-1] == cur:
    stack.pop()
    cur += 1

print("Nice" if not stack else "Sad")