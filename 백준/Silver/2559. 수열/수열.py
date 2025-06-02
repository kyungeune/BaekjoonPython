import sys
input = sys.stdin.readline

n, k = map(int, input().split())
mapping = list(map(int, input().split()))

# n은 전체 날짜의 수
# k는 연속적인 날짜의 수
window_sum = sum(mapping[:k])
max_sum=window_sum

for i in range(k, n):
    window_sum+=mapping[i]-mapping[i-k]
    max_sum=max(max_sum, window_sum)

print(max_sum)