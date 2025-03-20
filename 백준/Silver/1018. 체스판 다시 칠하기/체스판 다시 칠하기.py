import sys

p = []  # 체스판
min = 51  # 최소


x, y = map(int, input().split())


for i in range(x):
    p.append(list(sys.stdin.readline().strip()))

now = p[0][0] # W B 왔다갔다 할 변수



for i in range(x-7):
    for j in range(y-7):
        
        now = p[i][j]
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

        
        if p[i][j] == 'W':  # 두번비교
            now = 'B'
        else:
            now = 'W'
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