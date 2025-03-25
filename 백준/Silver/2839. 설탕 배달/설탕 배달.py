import sys

input = sys.stdin.readline

original = int(input())

min = 2000  # N<=5000이기 때문에 최대 봉지수는 5000/3<2000이기 때문에 min을 2000으로 잡아도 됨

# 아이디어
# 5봉지는 0개 1개 2개.. 점점 커져가고, 
# 나머지를 3으로 뺀 후 이 수가 
# 나누어 떨어지지 않으면 continue,
# 나누어 떨어지면 min과 비교

for i in range(original//3+1):  # 최대 봉지개수: 3으로 나눈 몫
    cnt = 0  # 매번 cnt를 담을 변수
    n = original

    for five in range(i):  # 5를 0~i번 빼본다. 
        n -= 5
        cnt+=1
    while n>=3:  # 나머지는 전부 3을 빼는데 사용한다.
        n-=3
        cnt+=1
    
    if n!=0:  # 정확하게 N킬로그램으로 나눠지지 않으면
        continue
    elif cnt<min:  # cnt가 최소값이면
        min=cnt
        

if min==2000:  # 초기 설정된 min값과 현재 min값이 같으면
    print("-1")
else:
    print(min)