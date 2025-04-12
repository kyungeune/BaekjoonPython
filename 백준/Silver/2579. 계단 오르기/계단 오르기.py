import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

if n==1:
    print(arr[0])
    exit()
elif n==2:
    print(arr[0]+arr[1])
    exit()


ans = [0]*n

ans[0]=arr[0]  # 첫번째 계단만 밟았을 때
ans[1]=arr[0]+arr[1]  # 첫번째 -> 두번째
ans[2]=max(arr[0]+arr[2], arr[1]+arr[2])  # 두 가지 경우 중 더 큰 걸 선택 0->2 || 1->2

for i in range(3,n):
    ans[i]=max(ans[i-2]+arr[i], ans[i-3]+arr[i-1]+arr[i])  # 연속으로 3칸을 밟는 경우는 없음

print(ans[n-1])

# k = 0  # 현재 연속된 칸
# sum = arr[0]
# for i in range(n-2):
#     if i == n-5:
#         if k == 1:
#             sum += max(arr[n-3]+arr[n-1], arr[n-2])
#             sum += arr[n-1]
#         else:
#             sum += max(arr[n-2], arr[n-1])
#             sum += arr[n-1]
#     elif i == n-4:
#         sum += max(arr[n-3], arr[n-2])
#         sum += arr[n-1] # 마지막 수 더하기
#         break
#     elif (arr[i+1]>arr[i+2]) and k<2:  # 두칸연속밟으면
#         sum += arr[i+1]
#         k = 2
#     else:
#         sum += arr[i+2]
#         i += 1
#         k = 1


# print(sum)