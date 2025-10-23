def solution(s):
    answer = []
    
    a = 0
    wheel = 0
    # x의 모든 0을 제거한다
    while s!="1":
        x = ""
        for i in s:
            if i=="0":
                a+=1
            else:
                x+=i
        
        
        wheel += 1
        k = len(x)  # 7
        l = bin(k)[2:]
        s = str(l)
    
    answer.append(wheel)
    answer.append(a)
    return answer