import sys

input = sys.stdin.readline

original = int(input())

min = 2000

for i in range(original//3+1):
    cnt = 0
    n = original

    for five in range(i):
        n -= 5
        cnt+=1
    while n>=3:
        n-=3
        cnt+=1
    
    if n!=0:
        continue
    elif cnt<min:
        min=cnt
        

if min==2000:
    print("-1")
else:
    print(min)