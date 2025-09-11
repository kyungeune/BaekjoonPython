import sys
input = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, input().split())

num = {}

for i in range(n):
    a, b = input().strip().split()  # \n 제거를 위해
    num[a] = b
    

for _ in range(m):
    imsi = input().strip()
    write(num[imsi]+'\n')