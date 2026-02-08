from collections import Counter

def solution(topping):
    answer = 0
    a = set()  # 왼쪽부터 커지는 set
    b = set()  # 나머지 오른쪽
    length = len(topping)  # 전체 길이
    c = Counter(topping)  # 카운터
    
    # b의 unique 개수 미리 세두기
    for t in range(length):  
        b.add(topping[t])

    
    for t in range(length):
        x = topping[t]
        
        # 하나씩 더해가기
        a.add(x)  
        
        # 카운터 하나씩 빼기
        c[x] -= 1
        
        if c[x] == 0:  # 뒤에 없으면 빼기
            b.remove(x)
        
        # 개수 확인
        if len(a) == len(b):
            answer += 1
    
    return answer