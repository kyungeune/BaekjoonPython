import sys
input = sys.stdin.readline

n = int(input())
stack = []
sum = 0

for i in range(n):
    x = int(input())
    if x==0:
        sum -= stack.pop()
    else:
        sum += x
        stack.append(x)

print(sum)