import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())

# a = [1, 2, 3]
# print(*a)  # 출력: 1 2 3

def backtrack(result):
    if len(result)==m:
        print(*result)
        return
    
    for i in range(result[-1] if result else 1, n + 1):  # result가 비어있음 1부터, 아니면 맨 뒤 숫자부터
        backtrack(result + [i])  # 새로운 리스트를 만들어 전달

backtrack([])