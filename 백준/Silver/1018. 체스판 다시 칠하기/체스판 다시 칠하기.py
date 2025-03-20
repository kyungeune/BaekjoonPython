import sys

p = []  # 체스판
min = 51  # 최소

# 입력받기
x, y = map(int, input().split()) 
for i in range(x):  
    p.append(list(sys.stdin.readline().strip()))


for i in range(x-7):
    for j in range(y-7):
        
        now = 'B'  # 현재 위치에 있어야 하는 문자, 'B'로 시작하는 체스판
        cnt = 0  # 바꿔야 할 것 개수 담는 변수

        for r in range(i, i+8):
            for c in range(j, j+8):
                if now == 'W': # 화이트여야 하는데
                    if p[r][c] == 'B': # 블랙이면
                        cnt+=1
                    now = 'B' # 색 반전
                elif now == 'B':
                    if p[r][c] == 'W':
                        cnt+=1
                    now = 'W'
            
            if now == 'W': # 8*8 체스판이라 행으로 내려올 때 같은 숫자가 반복됨 --> 한 번 색반전 해주기 
                now = 'B'
            elif now == 'B':
                now = 'W'
                
        if cnt < min: # min 구하기
            min = cnt

        
        now = 'W' # 'W'로 시작하는 체스판
        cnt = 0

        for r in range(i, i+8):
            for c in range(j, j+8):
                if now == 'W':
                    if p[r][c] == 'B':
                        cnt+=1
                    now = 'B'
                elif now == 'B':
                    if p[r][c] == 'W':
                        cnt+=1
                    now = 'W'
            
            if now == 'W':
                now = 'B'
            elif now == 'B':
                now = 'W'
                
        if cnt < min:
            min = cnt


print(min)        