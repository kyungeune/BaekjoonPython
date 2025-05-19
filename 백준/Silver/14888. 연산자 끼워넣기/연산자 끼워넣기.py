import sys
input = sys.stdin.readline

def DFS(idx, total):  # idx : 몇번째, bIdx : 부호인덱스(전부 다 돌아야 함)
    global max, min, buho
    if idx == n:
        if total > max:
            max = total
        if total < min:
            min = total
        return
    
    for i in range(4):
        if buho[i]>=1:
            buho[i]-=1

            rslt=0
            if i==0:
                rslt = total + nums[idx]
            elif i==1:
                rslt = total - nums[idx]
            elif i==2:
                rslt = total * nums[idx]
            else:
                if total < 0:
                    rslt = -(-total // nums[idx])
                else:
                    rslt = total // nums[idx]

            DFS(idx+1, rslt)
            buho[i]+=1


n = int(input())
nums = list(map(int, input().split()))
buho = list(map(int, input().split()))
max=-1000000001
min = 1000000001

DFS(1, nums[0])

print(max)
print(min)