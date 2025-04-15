import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    x = input().strip()
    print(x[0]+x[-1])