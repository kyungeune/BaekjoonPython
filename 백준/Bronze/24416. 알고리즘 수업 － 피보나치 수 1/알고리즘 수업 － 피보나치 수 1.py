import sys
input = sys.stdin.readline

def fib(n):  # 재귀호출 오리지널 코드
    if n==1 or n==2:# 코드가 실행된 횟수 = return이 실행된 횟수
        return 1
    else:
        return (fib(n-1)+fib(n-2))

def fibonacci(n):  # 동적 프로그래밍 오리지널 코드
    arr = []
    arr.append(1)
    arr.append(1)

    for i in range(2, n):   
        arr.append(arr[i-1] + arr[i-2])
    
    return arr[n-1]




n = int(input())

# 실제로 실행하는 순간 시간초과

count = [0] * 41
count[1]=1
count[2]=1

for i in range(3, 41):  # 계산 미리 해두기
    count[i] = count[i-1] + count[i-2]

print(count[n], n-2)