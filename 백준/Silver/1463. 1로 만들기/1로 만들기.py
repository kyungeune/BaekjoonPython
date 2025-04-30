import sys
input = sys.stdin.readline

n = int(input())

x=[0]*(n+1)
x[0]=0
x[1]=0

for i in range(2,n+1):
    x[i]=x[i-1]+1  # 빼기 1 이 default
    if i%3==0: x[i]=min(x[i], x[i//3]+1)  # x[6]이면 x[2]=1 값에 +1을 해줘야 현재 내가 가리키는 값이 됨
    if i%2==0: x[i]=min(x[i], x[i//2]+1)

print(x[n])