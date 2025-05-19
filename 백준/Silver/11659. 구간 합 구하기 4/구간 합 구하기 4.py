import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# 시간초과 해결하자
hap = [0]*N
hap[0] = arr[0]
for i in range(1, N):
    hap[i] = hap[i-1] + arr[i]

start = []
end = []
for i in range(M):
    a,b=map(int, input().split())
    start.append(a)
    end.append(b)

for i in range(M):
    a = start[i]-1
    b = end[i]-1
    if a==0:  # 처음부터 구하는 경우
        print(hap[b])
    else:
        print(hap[b]-hap[a-1])

# 시간초과 남
# for i in range(M):
#     a = start[i]
#     b = end[i]
#     sum = 0
#     for j in range(a-1,b):
#         sum+=arr[j]
#     print(sum)