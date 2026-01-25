from collections import deque

def solution(s):
    answer = 0
    i, j = 0, 0
    
    # 가지치기
    if len(s) % 2 != 0:
        return 0
    
    q = deque()
    
    for i in s:
        q.append(i)
        
    # 끝
    for i in range(len(s)):
        nam = deque()
        finish = 1
        
        for j in range(len(s)):
            x = q[j]
            
            if not nam and (x == "}" or x == "]" or x == ")"):
                finish = 0
                break
            if (x == "{" or x == "[" or x == "("):
                nam.append(x)
                continue
            
            if nam[-1] == "(" and x == ")":
                nam.pop()
            elif nam[-1] == "{" and x == "}":
                nam.pop()
            elif nam[-1] == "[" and x == "]":
                nam.pop()
            else:
                finish = 0
                break
                
        if finish == 1 and not nam:
            answer += 1
        q.append(q.popleft())
    
    
    return answer