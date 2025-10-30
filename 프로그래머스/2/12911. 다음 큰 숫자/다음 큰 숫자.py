def solution(n):
    answer = 0
    
    k = bin(n)
    m = k.count("1")
    
    while n>0:
        n=n+1;
        
        nB = bin(n)
        nC = nB.count("1")
        if nC == m:
            answer = n
            break
        
    
    return answer