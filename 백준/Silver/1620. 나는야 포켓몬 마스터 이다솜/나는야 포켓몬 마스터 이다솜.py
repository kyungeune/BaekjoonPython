import sys
input = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, input().split())

num = {}
name = {}

for i in range(n):
    x = input().strip()  # \n 제거를 위해
    num[i] = x
    name[x] = i
    

for _ in range(m):
    imsi = input().strip()

    if imsi.isalpha():  # 문자열이면
        write(str(name[imsi]+1)+'\n')
    else:
        write(num[int(imsi)-1]+'\n')