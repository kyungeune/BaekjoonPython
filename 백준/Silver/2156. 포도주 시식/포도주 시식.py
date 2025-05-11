import sys
# 0. 입력 및 초기화
input = sys.stdin.readline

n = int(input())

po = [0]*n  # 포도주 잔
dp = [0]*n  # 최대 포도주 계산해나가며 저장


# 1. 포도주 잔 정보 입력
for i in range(n):
    po[i] = int(input())

# 2. 0~2번째 포도주 잔 설정
dp[0]=po[0]
if n==2:
    dp[1]=po[1]+po[0]
elif n>=3:
    dp[1]=po[1]+po[0]
    dp[2]=max(po[0]+po[2], po[1]+po[2], po[0]+po[1])

# 3. for문을 돌며 dp 채우기
for i in range(3, n):
    dp[i] = dp[i-3]+po[i-1]+po[i]
    dp[i] = max(dp[i], dp[i-2]+po[i])
    dp[i] = max(dp[i], dp[i-1])

print(dp[n-1])