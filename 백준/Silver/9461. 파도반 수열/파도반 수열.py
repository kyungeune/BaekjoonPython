import sys
input = sys.stdin.readline

n = int(input())  # 테스트케이스 입력받기
pt = []
for i in range(n):
    x = int(input())
    pt.append(x)

ar = [0]*(max(pt)+1)
ar[1] = 1
ar[2] = 1
ar[3] = 1
ar[4] = 2
ar[5] = 2
ar[6] = 3
ar[7] = 4
ar[8] = 5
ar[9] = 7
ar[10] = 9
ar[11] = 12
ar[12] = 16

for i in range(13, max(pt)+1):
    ar[i] = ar[i-1] + ar[i-5]

for i in range(n):
    print(ar[pt[i]])