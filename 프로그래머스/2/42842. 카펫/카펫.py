def solution(brown, yellow):
    answer = []
    
    
    #  ******
    # *      *
    # *      *
    # *      *
    # *      *
    #  ******
    #  *
    # * *
    #  *
    brown -= 4
    for i in range(1,brown):
        if yellow % i !=0:
            continue
        if (yellow / i) * 2 + i*2 == brown:
            answer.append((yellow / i)+2)
            answer.append(i+2)
            break
        
    
    return answer