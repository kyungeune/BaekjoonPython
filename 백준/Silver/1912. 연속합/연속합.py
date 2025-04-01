import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

least = arr[0]  # 합의 최대를 담기
high = arr[0]  # 찐최댓값

for i in range(1, n):
    least = max(arr[i], least + arr[i])
    high = max(high, least)

print(high)