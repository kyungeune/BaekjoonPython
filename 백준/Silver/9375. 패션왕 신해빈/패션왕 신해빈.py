import sys
input = sys.stdin.readline

n = int(input())

sp = []
for i in range(n):
    dic = {}  # 딕셔너리 초기화
    m = int(input())

    for _ in range(m):
        a, b = input().split()
        if dic.get(b,0) == 0:  # 딕셔너리에 키 값이 없으면
            dic[b] = 2  # 새로운 키값 생성
        else:
            dic[b]+=1  # 키 값이 존재한다면 +1
    
    answer = 1
    for keys in dic.keys():
        answer *= dic[keys]

    print(answer-1)