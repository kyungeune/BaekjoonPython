import sys

input = sys.stdin.readline

# 기존 랜선 k개
# n개를 만들고 싶음
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start=1
end = max(arr)
result = 0

while start<=end:
    mid = (start+end)//2
    cnt = sum(i // mid for i in arr)

    if cnt>=n:
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)