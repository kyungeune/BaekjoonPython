import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

for i in arr:
    print(i)

# 항목	input()	        sys.stdin.readline()
# 속도	느림	        빠름
# 개행 처리	자동 제거	\n이 포함됨 → .strip() 필요할 수도
# 사용처	작은 입력	백준처럼 큰 입력