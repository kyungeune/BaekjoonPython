# 동적 계획법
import sys
input = sys.stdin.readline

n = int(input())

x = []
for i in range(n):
    x.append(int(input()))

# 사전작업
largest = max(x)
arr = [0]*(largest+1)
arr[1] = 1
arr[2] = 2
arr[3] = 4
# 제일 큰 수 만큼!
for i in range(4, largest+1):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

# 출력해주기
for i in x:
    print(arr[i])