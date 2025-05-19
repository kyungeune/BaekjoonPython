import sys
input = sys.stdin.readline

def DFS(idx, total):  # idx : 몇번째
    global max, min, buho
    if idx == n:
        if total > max:
            max = total
        if total < min:
            min = total
        return
    
    for i in range(4):  # 부호 회전
        if buho[i]>=1:
            buho[i]-=1

            rslt=0
            if i==0:
                rslt = total + nums[idx]
            elif i==1:
                rslt = total - nums[idx]
            elif i==2:
                rslt = total * nums[idx]
            else:  # 나누기
                if total < 0:
                    rslt = -(-total // nums[idx])
                else:
                    rslt = total // nums[idx]

            DFS(idx+1, rslt)
            buho[i]+=1  # 되돌리기


n = int(input())
nums = list(map(int, input().split()))
buho = list(map(int, input().split()))
max=-1000000001
min = 1000000001

DFS(1, nums[0])  # 첫번째 값을 넣은 채로 진행

print(max)
print(min)